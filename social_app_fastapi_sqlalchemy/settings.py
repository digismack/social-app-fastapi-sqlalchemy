SOCIAL_AUTH_SAML_SP_ENTITY_ID = "https://github.com/omab/python-social-auth/saml-test"
SOCIAL_AUTH_SAML_SP_PUBLIC_CERT = "MIICsDCCAhmgAwIBAgIJAO7BwdjDZcUWMA0GCSqGSIb3DQEBBQUAMEUxCzAJBgNVBAYTAkNBMRkwFwYDVQQIExBCcml0aXNoIENvbHVtYmlhMRswGQYDVQQKExJweXRob24tc29jaWFsLWF1dGgwHhcNMTUwNTA4MDc1ODQ2WhcNMjUwNTA3MDc1ODQ2WjBFMQswCQYDVQQGEwJDQTEZMBcGA1UECBMQQnJpdGlzaCBDb2x1bWJpYTEbMBkGA1UEChMScHl0aG9uLXNvY2lhbC1hdXRoMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCq3g1Cl+3uR5vCnN4HbgjTg+m3nHhteEMyb++ycZYre2bxUfsshER6x33l23tHckRYwm7MdBbrp3LrVoiOCdPblTml1IhEPTCwKMhBKvvWqTvgfcSSnRzAWkLlQYSusayyZK4n9qcYkV5MFni1rbjx+Mr5aOEmb5u33amMKLwSTwIDAQABo4GnMIGkMB0GA1UdDgQWBBRRiBR6zS66fKVokp0yJHbgv3RYmjB1BgNVHSMEbjBsgBRRiBR6zS66fKVokp0yJHbgv3RYmqFJpEcwRTELMAkGA1UEBhMCQ0ExGTAXBgNVBAgTEEJyaXRpc2ggQ29sdW1iaWExGzAZBgNVBAoTEnB5dGhvbi1zb2NpYWwtYXV0aIIJAO7BwdjDZcUWMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQEFBQADgYEAJwsMU3YSaybVjuJ8US0fUhlPOlM40QFCGL4vB3TEbb24Mq8HrjUwrU0JFPGls9a2OYzN2B3e35NorMuxs+grGtr2yP6LvuX+nV6A93wb4ooGHoGfC7VLlyxSSns937SS5R1pzQ4gWzZma2KGWKICWph5zQ0ARVhL63967mGLmoI="
SOCIAL_AUTH_SAML_SP_PRIVATE_KEY = "MIICXgIBAAKBgQCq3g1Cl+3uR5vCnN4HbgjTg+m3nHhteEMyb++ycZYre2bxUfsshER6x33l23tHckRYwm7MdBbrp3LrVoiOCdPblTml1IhEPTCwKMhBKvvWqTvgfcSSnRzAWkLlQYSusayyZK4n9qcYkV5MFni1rbjx+Mr5aOEmb5u33amMKLwSTwIDAQABAoGBAIHAg6NJSiYC/NYpVzWfKlasuoNy78R5adXYSNZiCR5V5FNm5OzmODZgXUt6g0A7FomshIT/txQWoV7y5FmwPs8n13JY3Hdt4tJ6MHw2feLo710+OEp9VBQus3JsB2F8ONYrGvs00hPPL7h5av/rzTdE8F67YM1mSgeg7xEF6BghAkEA12OOqSzp2MLTNY7PqOaLDzy4aAMVNN3Ntv2jBN0jq7s1b5ilQ2PGkLwdtkicq/VZcRyUqVbZbMwz05II3nqx3wJBAMsVhRQ5sdFCRBzEbSAm2YEJaFh5u6QT3+zWHMFpPJRnaBAWz3RXKEnleJ+DS2Xz1Jm6ZrmLdZiwMx/8dK5rDZECQQC7GTdWi7ZC3dIcpwaKIGHRhZxmda8ZMkc9Wwwd8H7I8aFUZFPCu0xEc7SXoHHACit8zyfwBYpvMN8gPK3JnOkfAkEAsUSpk0wBMT38one7IZOHzCDgGkq4RbKrhdon45Pus0PIDDM9BrqFimtpbSN4DxhVfZK91DwtfAhhuAvv9cewYQJAPMhpAqv3PBGYmtRDUlWXJQv2JRJJkrvbbqgBed2OX5RRgj5V3SR6PBhLbcTZ+q+1tdPkMFzZo5U6MN5m/6oXvQ=="
SOCIAL_AUTH_SAML_SECURITY_CONFIG = {"wantAttributeStatement": False, "wantNameId": False}
SOCIAL_AUTH_SAML_ORG_INFO = {
    "en-US": {"name" : "psa", "displayname": "PSA", "url": "https://github.com/omab/python-social-auth/"}
}
SOCIAL_AUTH_SAML_TECHNICAL_CONTACT = {"givenName": "Tech Gal", "emailAddress": "technical@example.com"}
SOCIAL_AUTH_SAML_SUPPORT_CONTACT = {"givenName": "Support Guy", "emailAddress": "support@example.com"}
SOCIAL_AUTH_SAML_ENABLED_IDPS = {
    "testshib": {
        "entity_id": "https://idp.testshib.org/idp/shibboleth",
        "url": "https://idp.testshib.org/idp/profile/SAML2/Redirect/SSO",
        "x509cert" : "MIIEDjCCAvagAwIBAgIBADANBgkqhkiG9w0BAQUFADBnMQswCQYDVQQGEwJVUzEVMBMGA1UECBMMUGVubnN5bHZhbmlhMRMwEQYDVQQHEwpQaXR0c2J1cmdoMREwDwYDVQQKEwhUZXN0U2hpYjEZMBcGA1UEAxMQaWRwLnRlc3RzaGliLm9yZzAeFw0wNjA4MzAyMTEyMjVaFw0xNjA4MjcyMTEyMjVaMGcxCzAJBgNVBAYTAlVTMRUwEwYDVQQIEwxQZW5uc3lsdmFuaWExEzARBgNVBAcTClBpdHRzYnVyZ2gxETAPBgNVBAoTCFRlc3RTaGliMRkwFwYDVQQDExBpZHAudGVzdHNoaWIub3JnMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArYkCGuTmJp9eAOSGHwRJo1SNatB5ZOKqDM9ysg7CyVTDClcpu93gSP10nH4gkCZOlnESNgttg0r+MqL8tfJC6ybddEFB3YBo8PZajKSe3OQ01Ow3yT4I+Wdg1tsTpSge9gEz7SrC07EkYmHuPtd71CHiUaCWDv+xVfUQX0aTNPFmDixzUjoYzbGDrtAyCqA8f9CN2txIfJnpHE6q6CmKcoLADS4UrNPlhHSzd614kR/JYiks0K4kbRqCQF0Dv0P5Di+rEfefC6glV8ysC8dB5/9nb0yh/ojRuJGmgMWHgWk6h0ihjihqiu4jACovUZ7vVOCgSE5Ipn7OIwqd93zp2wIDAQABo4HEMIHBMB0GA1UdDgQWBBSsBQ869nh83KqZr5jArr4/7b+QazCBkQYDVR0jBIGJMIGGgBSsBQ869nh83KqZr5jArr4/7b+Qa6FrpGkwZzELMAkGA1UEBhMCVVMxFTATBgNVBAgTDFBlbm5zeWx2YW5pYTETMBEGA1UEBxMKUGl0dHNidXJnaDERMA8GA1UEChMIVGVzdFNoaWIxGTAXBgNVBAMTEGlkcC50ZXN0c2hpYi5vcmeCAQAwDAYDVR0TBAUwAwEB/zANBgkqhkiG9w0BAQUFAAOCAQEAjR29PhrCbk8qLN5MFfSVk98t3CT9jHZoYxd8QMRLI4j7iYQxXiGJTT1FXs1nd4Rha9un+LqTfeMMYqISdDDI6tv8iNpkOAvZZUosVkUo93pv1T0RPz35hcHHYq2yee59HJOco2bFlcsH8JBXRSRrJ3Q7Eut+z9uo80JdGNJ4/SJy5UorZ8KazGj16lfJhOBXldgrhppQBb0Nq6HKHguqmwRfJ+WkxemZXzhediAjGeka8nz8JjwxpUjAiSWYKLtJhGEaTqCYxCCX2Dw+dOTqUzHOZ7WKv4JXPK5G/Uhr8K/qhmFT2nIQi538n6rVYLeWj8Bbnl+ev0peYzxFyF5sQA=="
    },
    "other": {
        "entity_id": "https://unused.saml.example.com",
        "url": "https://unused.saml.example.com/SAML2/Redirect/SSO"
    }
}
