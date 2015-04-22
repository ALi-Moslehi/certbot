"""Let's Encrypt constants."""
import logging
import pkg_resources

from letsencrypt.acme import challenges


SETUPTOOLS_PLUGINS_ENTRY_POINT = "letsencrypt.plugins"
"""Setuptools entry point group name for plugins."""


# CLI/IConfig defaults
DEFAULT_CONFIG_FILES = ["/etc/letsencrypt/cli.ini"]
DEFAULT_VERBOSE_COUNT = -(logging.WARNING / 10)
DEFAULT_SERVER = "letsencrypt-demo.org:443"
DEFAULT_RSA_KEY_SIZE = 2048
DEFAULT_ROLLBACK_CHECKPOINTS = 0
DEFAULT_CONFIG_DIR = "/etc/letsencrypt"
DEFAULT_WORK_DIR = "/var/lib/letsencrypt"
DEFAULT_BACKUP_DIR = "/var/lib/letsencrypt/backups"
DEFAULT_KEY_DIR = "/etc/letsencrypt/keys"
DEFAULT_CERTS_DIR = "/etc/letsencrypt/certs"
DEFAULT_CERT_PATH = "/etc/letsencrypt/certs/cert-letsencrypt.pem"
DEFAULT_CHAIN_PATH = "/etc/letsencrypt/certs/chain-letsencrypt.pem"


S_SIZE = 32
"""Size (in bytes) of secret base64-encoded octet string "s" used in
challenges."""

NONCE_SIZE = 16
"""Size of nonce used in JWS objects (in bytes)."""


EXCLUSIVE_CHALLENGES = frozenset([frozenset([
    challenges.DVSNI, challenges.SimpleHTTPS])])
"""Mutually exclusive challenges."""


ENHANCEMENTS = ["redirect", "http-header", "ocsp-stapling", "spdy"]
"""List of possible :class:`letsencrypt.client.interfaces.IInstaller`
enhancements.

List of expected options parameters:
- redirect: None
- http-header: TODO
- ocsp-stapling: TODO
- spdy: TODO

"""


DVSNI_CHALLENGE_PORT = 443
"""Port to perform DVSNI challenge."""


TEMP_CHECKPOINT_DIR = "temp_checkpoint"
"""Temporary checkpoint directory (relative to IConfig.work_dir)."""

IN_PROGRESS_DIR = "IN_PROGRESS"
"""Directory used before a permanent checkpoint is finalized (relative to
IConfig.work_dir)."""

CERT_KEY_BACKUP_DIR = "keys-certs"
"""Directory where all certificates and keys are stored (relative to
IConfig.work_dir. Used for easy revocation."""

REC_TOKEN_DIR = "recovery_tokens"
"""Directory where all recovery tokens are saved (relative to
IConfig.work_dir)."""

NETSTAT = "/bin/netstat"
"""Location of netstat binary for checking whether a listener is already
running on the specified port (Linux-specific)."""
