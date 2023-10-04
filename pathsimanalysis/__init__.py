"""
PathSimAnalysis
Calculates the geometric similary of molecular dynamics trajectories using path metrics such as the Hausdorff and Fréchet distances.
"""

# Add imports here

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
