# Simple Shared Key Mutual Authentication

Shared key mutual authentication allows secure communication between two parties, like Alice and Bob, who share a secret key.

1. Alice initiates by sending a random challenge.
2. Bob encrypts this challenge with the shared key and sends it back.
3. Alice decrypts it with the same key.
4. If successful, she knows Bob has the key.
5. Then, Alice sends her own challenge, and Bob repeats the process.

This confirms both parties' identities and allows them to communicate securely.

# Running the Algorithm

Clone the repository to a local folder.

CD into the folder.

Run the following to create a virtual environment:

```bash
python3 -m venv env
```

Activate the virtual environment (Ubuntu/Linux):

```bash
source env/bin/active
```

Run the program:

```bash
python3 sskma.py
```

Follow the prompts!
