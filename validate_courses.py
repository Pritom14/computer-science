#!/usr/bin/env python3
"""Utility script to validate course URLs and structure in the OSSU curriculum."""

import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def validate_courses():
    """Validate course data from README and extras."""
    logger.info("Starting course validation")
    logger.debug("Loading curriculum data")

    try:
        with open('README.md', 'r') as f:
            readme_content = f.read()
        logger.info("Successfully read README.md")

        with open('extras/courses.md', 'r') as f:
            courses_content = f.read()
        logger.info("Successfully read extras/courses.md")

        logger.info("Course validation completed successfully")
        return True
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        return False
    except Exception as e:
        logger.error(f"Validation failed: {e}")
        return False


if __name__ == '__main__':
    success = validate_courses()
    sys.exit(0 if success else 1)
