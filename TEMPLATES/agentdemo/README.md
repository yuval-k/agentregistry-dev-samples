# agentdemo — dice-rolling ADK-Python agent

A minimal Google ADK agent that rolls dice and checks primes. Useful as a
starting point for any ADK-Python agent you want to build and publish to
agentregistry.

**Fork the parent repo first, then copy this template out.** Do not edit it
in place.

```bash
cp -R TEMPLATES/agentdemo ./my-agent
cd ./my-agent
# edit agent.yaml → set the image name you'll push to
arctl agent build .
arctl agent run .
```

## What's inside

- `agent/agent.py` — the ADK `root_agent` with two built-in tools (`roll_die`,
  `check_prime`). Add MCP tools later via `arctl agent add-mcp`.
- `agent.yaml` — the registry manifest.
- `Dockerfile` — builds on `ghcr.io/kagent-dev/kagent/kagent-adk`.
- `pyproject.toml` — pins `google-adk`.

## Expected env

- `GOOGLE_API_KEY` — required for `arctl agent run` (Gemini).
- `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` — optional; unset ⇒ no tracing.
