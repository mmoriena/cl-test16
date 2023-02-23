{
    "name": "test15",
    "version": "15.0.1.0.0",
    "category": "Tools",
    "summary": "Proyect module for test15",
    "author": "mmoriena",
    "website": "mmoriena.com",
    "license": "AGPL-3",
    "depends": [
        "sale",
    ],
    "installable": True,
    "env-ver": "2",
    "odoo-license": "CE",
    "config": [
        "workers = 0",
        "max_cron_threads = 1",
        "limit_request = 8192",
        "limit_memory_soft = 2147483648",
        "limit_memory_hard = 2684354560",
    ],
    "port": "8069",
    "git-repos": [
        "https://github.com/mmoriena/cl-test16.git",
        # OCA
        "https://github.com/OCA/brand oca-brand",
        "https://github.com/OCA/web oca-web",
        "https://github.com/OCA/stock-logistics-workflow",
        "https://github.com/OCA/purchase-workflow.git",
        # ingadhoc
        "https://github.com/ingadhoc/account-financial-tools adhoc-account-financial-tools",
        "https://github.com/ingadhoc/account-payment adhoc-account-payment",
        "https://github.com/ingadhoc/aeroo_reports.git",
        "https://github.com/ingadhoc/argentina-sale adhoc-argentina-sale",
        "https://github.com/ingadhoc/odoo-argentina adhoc-odoo-argentina",
        "https://github.com/ingadhoc/odoo-argentina-ee adhoc-odoo-argentina-ee",
        "https://github.com/ingadhoc/stock adhoc-stock",
    ],
    # list of images to use in the form 'name image-url'
    "docker-images": [
        "odoo jobiols/odoo-jeo:15.0",
        "postgres postgres:14.2-alpine",
    ],
}
