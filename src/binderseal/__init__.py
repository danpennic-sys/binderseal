"""BinderSeal — local-first evidence binder sealer for QuantumGuard CONTRACT-v1."""

from .core import (
    __version__,
    build_evidence_pack,
    collect_files,
    load_or_create_key,
    main,
    sha256_hex,
)

__all__ = [
    "__version__",
    "build_evidence_pack",
    "collect_files",
    "load_or_create_key",
    "main",
    "sha256_hex",
]
