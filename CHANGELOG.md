# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!--
The rules for this file:
  * entries are sorted newest-first.
  * summarize sets of changes - don't reproduce every git log comment here.
  * don't ever delete anything.
  * keep the format consistent:
    * do not use tabs but use spaces for formatting
    * 79 char width
    * YYYY-MM-DD date format (following ISO 8601)
  * accompany each entry with github issue/PR number (Issue #xyz)
-->

## [Unreleased]

### Authors
<!-- GitHub usernames of contributors to this release -->
- ianmkenney

### Added
<!-- New added features -->
- GitHub action workflow for automatic PyPI package deployment (PR #3)

### Fixed
<!-- Bug fixes -->

### Changed
<!-- Changes in existing functionality -->

### Deprecated
<!-- Soon-to-be removed features -->

### Removed
<!-- Removed features -->

## [1.0.0] -- 2023-10-10

pathsimanalysis was created by Ian Kenney in 2023 and is based upon the 
source code in the MDAnalysis.analysis.psa analysis submodule originally
authored by Sean Seyler in 2015. Additional contributors to the original
source are reflected in the AUTHORS.md file contained in this repository.

### Added

- the core functionality of PathSimAnalysis (and its tests) was implemented
  using the source code from MDAnalysis.analysis.psa
- PRs trigger Read the Docs for debugging documentation (PR #1)
- GitHub actions workflow for building and deploying docs to GitHub pages 
  (PR #2)

[Unreleased]: https://github.com/MDAnalysis/PathSimAnalysis/compare/1.0.0...HEAD
[1.0.0]: https://github.com/MDAnalysis/PathSimAnalysis/releases/tag/1.0.0