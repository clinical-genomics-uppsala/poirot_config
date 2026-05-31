# Poirot config harmonization notes

This repository currently owns the production site overlays for
`poirot_rd_wgs`.

## Added in this pass

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
- Move remaining absolute paths behind a common `cgu/library` layout so site
  config only needs the installation parent and runtime resources.
- Keep CPU/GPU as execution modes, not cluster-specific config filenames.
