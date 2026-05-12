def test_import_asdf_wcs_schemas():
    """Test basic import of asdf_wcs_schemas package."""
    import asdf_wcs_schemas
    assert hasattr(asdf_wcs_schemas, '__version__')
