import jsonschema

def verify_certificate(cert: dict) -> None:
    """
    Validate a CVRE certificate.
    Raises on failure. Silent on success.
    """
    schema = cert.get("_schema_obj")
    if schema is None:
        raise ValueError("missing schema object")

    jsonschema.validate(instance=cert, schema=schema)
