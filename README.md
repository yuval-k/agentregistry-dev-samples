# agentregistry-dev-samples

Sample agents and MCP servers for [agentregistry](https://github.com/agentregistry-dev/agentregistry).
The goal of this repo is simple: give anyone trying out agentregistry a
known-good starting point so they don't have to bootstrap from scratch.

## 🍴 These are templates — fork, don't push

Everything under `TEMPLATES/` is meant to be **forked and adapted**, not
edited in place. If you push directly to this repo's `TEMPLATES/` other
people's demos break.

Intended workflow:

1. **Fork this repo** to your own GitHub account.
2. In your fork, copy the template you want into a new top-level directory:
   ```bash
   cp -R TEMPLATES/agentdemo ./my-agentdemo
   ```
3. Edit freely. Change the agent name, swap the model, add MCP servers,
   whatever you need. The template is a starting point, not a contract.
4. Commit and push to your fork. That's the URL you give to `arctl agent
   publish --github …`.

To contribute a *new* template (not a personal variant), open a PR against
this repo — see [Adding a new template](#adding-a-new-template).

## Templates

| Path | What it is |
|------|------------|
| [`TEMPLATES/agentdemo/`](TEMPLATES/agentdemo/) | Minimal ADK-Python agent with a dice-rolling and prime-checking tool. |
| [`TEMPLATES/everything-server/`](TEMPLATES/everything-server/) | MCP server exposing `echo`, `now`, `add`, and `reverse` tools. |

Each template has its own `README.md` with build and run instructions.

## Adding a new template

1. Add it under `TEMPLATES/<name>/` with a short `README.md` explaining what
   it does and how to build it.
2. Keep each template self-contained (no cross-template imports).
3. Templates must build using only public dependencies — no private image
   refs, no internal packages — so any fork is usable from a clean machine.
