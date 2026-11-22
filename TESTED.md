# What was tested, and on what

Tested 2026-11-21 on one Windows 10 desktop (Intel i7, 32 GB RAM, NVIDIA GTX 1660 Ti with 6 GB) with Ollama 0.40.16. These are single runs, not benchmarks. Your computer will be faster or slower.

| Test | Model | Result |
|---|---|---|
| 1,002-word transcript, one factual question | llama3.2:3b (about 2 GB) | Correct, 14 seconds after the model was loaded (116 seconds on the very first run while it loaded) |
| 204-word meeting notes (`sample/notes.txt`), action items | llama3.2:3b | Found five items in 12 seconds; four owners right, one wrong (it said Marcus would run the phishing training; the notes say he will ask the security group if someone can) |
| 29,812-word podcast transcript, "what is the format pyramid and what are its four levels?" | llama3.2:3b | About 4 minutes. It said the text did not mention the pyramid. It does, near the start. |
| Same transcript, same question | gemma4:e4b (about 6.6 GB) | About 8.5 minutes. All four levels correct (checked against the transcript). |

Not measured, so not claimed: dollars saved on Claude, speed on other computers, whether Claude always follows the CLAUDE.md rule.

Lesson: a small intern is fast and free and can miss things; a bigger one is slower and more careful; neither replaces looking at the answer.
