Decision: Bootstrap Script Behavior

Decision

bootstrap.sh shall be idempotent. Running it multiple times must not destroy an existing development environment.

Reason

Safe to execute repeatedly.
Predictable behavior.
Easier automation.
Easier CI/CD integration.
Can later support --force if a clean setup is required.
