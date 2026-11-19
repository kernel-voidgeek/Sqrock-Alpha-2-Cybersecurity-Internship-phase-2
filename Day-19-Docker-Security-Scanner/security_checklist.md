
# Docker Container Security Checklist

## Image Security
- [ ] Avoid using the latest image tag.
- [ ] Pin images to a specific version.
- [ ] Use trusted and maintained base images.
- [ ] Scan container images for known vulnerabilities.

## User Privileges
- [ ] Create a dedicated non-root user.
- [ ] Include an explicit USER instruction.
- [ ] Avoid unnecessary privileged permissions.

## Network Security
- [ ] Expose only required ports.
- [ ] Avoid exposing SSH (port 22) unnecessarily.
- [ ] Restrict network access where possible.

## Build Security
- [ ] Avoid storing secrets in Dockerfiles.
- [ ] Use multi-stage builds where appropriate.
- [ ] Minimize unnecessary packages.
- [ ] Review configuration before deployment.

## Runtime Security
- [ ] Apply resource limits.
- [ ] Use read-only filesystems when appropriate.
- [ ] Avoid privileged containers.
- [ ] Monitor container activity.
