# Copyright 2022 Berezi Amubieta - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Stock Picking Batch Liquidation",
    "version": "14.0.1.0.0",
    "author": "Avanzosc",
    "category": "Inventory",
    "depends": [
        "account",
        "analytic",
        "stock_account",
        "stock_picking_type_category",
        "stock_picking_batch",
        "stock_picking_batch_farmer",
        "stock_move_line_cost",
        "stock_picking_batch_mother",
        "stock_picking_batch_breeding",
        "custom_breeding_apps",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/account_move_line_decimal_precision.xml",
        "data/product_category_move_type.xml",
        "data/account_analytic_line_tag.xml",
        "views/stock_picking_batch_view.xml",
        "views/stock_inventory_view.xml",
        "views/stock_inventory_line_view.xml",
        "views/feed_rate_view.xml",
        "views/product_category_view.xml",
        "views/liquidation_contract_view.xml",
        "views/liquidation_contract_line_view.xml",
        "views/move_type_view.xml",
        "views/stock_move_line_view.xml",
        "views/stock_move_view.xml",
        "views/product_template_view.xml",
        "views/stock_warehouse_view.xml",
        "views/liquidation_line_view.xml",
        "views/account_move_view.xml",
        "views/account_analytic_line_view.xml",
    ],
    "license": "AGPL-3",
    "installable": True,
}
