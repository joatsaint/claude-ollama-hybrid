"""ask_local.py: the intern. Reads a long file with a free local Ollama model and prints a short answer.

Usage:
    python ask_local.py <file> "what you want to know"
    python ask_local.py <file> "what you want to know" --model gemma4:e4b
    python ask_local.py --check            (is Ollama running, and which models do you have?)

Needs: Ollama running on this computer and one model pulled. Python 3 only, no extra installs.
What it does: cuts the file into pieces, asks the local model about each piece, then asks it once more to
combine its notes into one short answer. Text only goes to your own computer (localhost), never to the internet.
Honest limit: small local models make mistakes and can miss things. Treat the answer as a good first pass and
spot-check anything that matters.
"""
import argparse
import json
import sys
import time
import urllib.error
import urllib.request

BASE = "http://localhost:11434"
DEFAULT_MODEL = "llama3.2:3b"


def call(path, payload=None, timeout=900):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(BASE + path, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


def friendly_exit(err, model):
    if isinstance(err, urllib.error.HTTPError) and err.code == 404:
        print(f"Ollama does not have the model '{model}'. Get it with:  ollama pull {model}", file=sys.stderr)
    elif isinstance(err, urllib.error.URLError):
        print("Cannot reach Ollama. Start the Ollama app (or run:  ollama serve ) and try again.", file=sys.stderr)
    else:
        print(f"Something went wrong: {err}", file=sys.stderr)
    sys.exit(1)


def ask(model, prompt, num_ctx=8192):
    out = call("/api/generate", {"model": model, "prompt": prompt, "stream": False, "options": {"num_ctx": num_ctx, "temperature": 0.2}})
    return out["response"].strip(), out.get("prompt_eval_count", 0), out.get("eval_count", 0)


def pieces(text, words_per_piece):
    w = text.split()
    for i in range(0, len(w), words_per_piece):
        yield " ".join(w[i:i + words_per_piece])


def check():
    try:
        tags = call("/api/tags", timeout=10)
    except Exception as e:
        friendly_exit(e, "")
    names = [m["name"] for m in tags.get("models", [])]
    print("Ollama is running.")
    print("Models you have:", ", ".join(names) if names else "none yet. Get one with:  ollama pull llama3.2:3b")


def main():
    ap = argparse.ArgumentParser(description="Read a long file with a local model and print a short answer.")
    ap.add_argument("file", nargs="?")
    ap.add_argument("question", nargs="?")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--piece", type=int, default=1500, help="words per piece (default 1500)")
    ap.add_argument("--check", action="store_true", help="test that Ollama is running and list your models")
    a = ap.parse_args()
    if a.check:
        return check()
    if not a.file or not a.question:
        ap.error("give a file and a question, or use --check")
    try:
        text = open(a.file, encoding="utf-8", errors="ignore").read()
    except OSError as e:
        print(f"Cannot read {a.file}: {e}", file=sys.stderr)
        sys.exit(1)
    words = len(text.split())
    t0 = time.time()
    notes, used_in, used_out = [], 0, 0
    try:
        for n, p in enumerate(pieces(text, a.piece), 1):
            prompt = (f"Read this part of a document. Write short bullet notes that help answer: {a.question}\n"
                      f"Only use facts from the text. If nothing is relevant, write NONE.\n\nTEXT:\n{p}")
            out, i, o = ask(a.model, prompt)
            used_in += i
            used_out += o
            if out.strip().upper() != "NONE":
                notes.append(out)
            print(f"  piece {n} done", file=sys.stderr)
        final = (f"Here are notes from a long document. Write a short answer (under 200 words) to: {a.question}\n"
                 f"Only use the notes.\n\nNOTES:\n" + "\n".join(notes))
        answer, i, o = ask(a.model, final)
    except Exception as e:
        friendly_exit(e, a.model)
    used_in += i
    used_out += o
    print(answer)
    print(f"\n[read {words} words with {a.model}; answer is {len(answer.split())} words; local tokens in/out {used_in}/{used_out}; {time.time() - t0:.0f}s]", file=sys.stderr)


if __name__ == "__main__":
    main()
