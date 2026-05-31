# Poirot config harmonization notes

This repository currently owns the production site overlays for
`poirot_rd_wgs`.

## Added in this pass

- `config/site/example.local.yaml`
- `config/site/miarka.local.yaml`
- `config/site/marvin.local.yaml`
- `profiles/slurm/config.yaml`
- `profiles/local/config.yaml`

The existing production files remain in place for compatibility:

- `config/config_production_pipeline.yaml`
- `config/config_production_pipeline.miarka.yaml`
- `profiles/production_cpu/config.yaml`
- `profiles/production_gpu/config.yaml`
- `profiles/miarka/config.yaml`

## Remaining refactor candidates

- Decide whether this config repo should remain separate or be packed as a
  versioned site-config bundle beside `poirot_rd_wgs`.
- Move remaining absolute paths from production overlays toward
  `REFERENCE_DATA_DIR`, `PACKAGED_REF_DIR`, `CONTAINER_DIR`, and
  `HYDRA_MODULES_DIR`.
- Keep CPU/GPU as execution modes, not cluster-specific config filenames.
