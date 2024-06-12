# Temporal Cloud Automation Tool
This is a simple sample python script about how you could orchestrate tcld to gather info about your Temporal Cloud namespaces.
For now all it does is list namespaces and users.
Before running, install tcld and login with tcld.

# Setup & Run:
1. Make sure you have [tcld](https://docs.temporal.io/cloud/tcld) installed and in your path
2. Log in with tcld
3. git clone this repo
4. execute the script
```bash
python cloud-manager.py
```
5. review the output:
```bash
$ cat namespace-list.csv
Namespace,
123-namespace.a2dd7,
josh-test.a2dd7,
demo-test1.a2dd7,
<snip>
```
```bash
$ cat user-list.csv 
Namespace,Email, Account Role, State
josh-test.a2dd7, user@email.com,Admin,Active,
josh-test.a2dd7, SDY@email.com,Admin,Active,
josh-test.a2dd7, user2@email.com,Admin,Active,
josh-test.a2dd7, user3@email.com,Admin,Active,
<snip>
```

**These examples are provided as-is, without support. They are intended as reference material only.**
