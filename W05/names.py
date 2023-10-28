# Step 1: Define the three main functions

def make_full_name(given_name, family_name):
    """Combine given name and family name into one string with family name first."""
    return f"{family_name}; {given_name}"

def extract_family_name(full_name):
    """Extract family name from the full name."""
    return full_name.split(";")[0].strip()

def extract_given_name(full_name):
    """Extract given name from the full name."""
    return full_name.split(";")[1].strip()
