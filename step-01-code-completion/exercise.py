import re


def normalize_username(name: str) -> str:
    # Trim outer whitespace
    name = name.strip()
    
    # Convert to lowercase
    name = name.lower()
    
    # Replace spaces with underscores
    name = name.replace(" ", "_")
    
    # Remove any character that is not a-z, 0-9, or underscore
    name = re.sub(r"[^a-z0-9_]", "", name)
    
    # Collapse repeated underscores into one underscore
    name = re.sub(r"_{2,}", "_", name)
    
    # Strip leading/trailing underscores
    name = name.strip("_")
    
    return name


def build_slug(title: str) -> str:
    # Lowercase
    slug = title.lower()
    
    # Replace any sequence of non-alphanumeric characters with a single '-'
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    
    # Strip leading/trailing '-'
    slug = slug.strip("-")
    
    return slug
