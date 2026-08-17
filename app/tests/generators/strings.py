import string
import secrets


def random_string(
    string_length: int,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_special: bool = True,
) -> str:
    """Creates a random string of given length

    Args:
        string_length: int
            Length of the expected string
        use_upper: bool
            True will include upper case letters and false won't
        use_digits: bool
            True will include digits and false won't
        use_special: bool
            True will include special characters and false won't

    Returns:
        str
            The string of expected length
    """
    
    characters: str = ''
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    return "".join(secrets.choice(characters) for _ in range(string_length))


def email(domain: str | None = None) -> str:
    """Creates a random email string with or without a specified domain.

    Args:
        domain: str | None
            The desired domain name in the string, example: ding.ck

    Returns:
        str
            The email string (with expected domain if specified)
    """

    if not domain:
        domain_name_length: int = int(secrets.choice(string.digits)) + 2
        domain_name: str = random_string(
            domain_name_length,
            use_upper=False,
            use_digits=True,
            use_special=False,
        )

        extension_length: int = secrets.choice([2, 3])
        extension: str = random_string(
            extension_length,
            use_upper=False,
            use_digits=False,
            use_special=False,
        )
        domain = f"{domain_name}.{extension}"

    email_id_length: int = int(secrets.choice(string.digits)) + 2
    email_id: str = random_string(
        email_id_length, use_upper=False, use_digits=True, use_special=False
    )

    return f"{email_id}@{domain}"

def mobile_string(length: int = 10) -> str:
    """Return a mobile number of string type

    Args:
        length: int
            The desired length of the mobile number (defaults to 10)

    Returns:
        str
            The mobile number of desired length in string format
    """
    return "".join(secrets.choice(string.digits) for _ in range(length))
