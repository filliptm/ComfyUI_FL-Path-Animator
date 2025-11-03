"""
FL Path Animator V2 - Standalone Node Pack
Creates animated shapes that follow user-drawn paths with visual editor.
"""

from .nodes.FL_PathAnimator import FL_PathAnimator

NODE_CLASS_MAPPINGS = {
    "FL_PathAnimatorV2": FL_PathAnimatorV2,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FL_PathAnimator": "FL Path Animator",
}

WEB_DIRECTORY = "./web"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]

print("\n" + "="*60)
print("FL Path Animator - Standalone Node Pack Loaded")
print("="*60 + "\n")
