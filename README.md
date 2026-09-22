# Aozix organization profile

This repository maintains the public GitHub homepage for [Aozix Technology](https://github.com/aozix-tech), with the same visual identity and English-language positioning as [aozix.com](https://aozix.com/).

## Files

- `profile/README.md` — the public organization homepage displayed by GitHub.
- `profile/assets/` — self-contained SVG banners and responsive capability cards.
- `scripts/build-profile.py` — the source for profile copy and generated visual assets.
- `scripts/check-profile.py` — offline checks for public links, English copy, accessible images, and safe SVG markup.

## Update

Edit `scripts/build-profile.py`, then run:

```sh
python3 scripts/build-profile.py
python3 scripts/check-profile.py
```

Changes to the generator trigger the profile publishing workflow, which validates and commits the generated profile. No external API credentials, paid services, fonts, or frontend dependencies are needed.

The artwork adapts the Aozix website's existing A mark, obsidian background, lavender and ice-blue palette, and orbital motif. SVGs are static, contain no scripts or embedded external resources, and have desktop and mobile layouts. Text alternatives describe the visual sections.

Only public brand and product information belongs here. Do not copy private application code, credentials, company-registration documents, or personal details into this public repository. The production website and its Cloudflare deployment remain in `aozix-tech/website` and are not modified by this repository.

Official links: [Website](https://aozix.com/) · [X — @aozixtech](https://x.com/aozixtech) · [Game support](https://games.sshd.one/support/).
