import dash
from dash import Input, Output, State, dcc, html, dash_table, ctx, ALL, MATCH
import dash_bootstrap_components as dbc

import pandas as pd

import component_function as comp_fun
import mba_function as mba_fun


trans_df = pd.read_csv("demo_trans.csv")
trans_df = trans_df.drop("Unnamed: 0", axis = 1)


app = dash.Dash(__name__,
                external_stylesheets = [dbc.themes.PULSE],
                suppress_callback_exceptions = True,
                meta_tags = [{"name": "viewport", "content": "width=device-width, initial-scale=1.0"}])
server = app.server

# Home =================================================================================================================
home_content = html.Div(
    [
        html.Div(
            html.H2("Market Basket Analysis"),
            className = "header-div",
        ),

        html.Br(),
        html.Br(),

        dbc.Container([
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Div(
                                [
                                    html.H5("Grouped Product Data"),
                                    dbc.NavLink(
                                        [
                                            dbc.Button("USE DATA", id = "use_product", n_clicks = 0),
                                        ],
                                        href = "/dashboard", active = "exact"
                                    ),

                                    html.Br(),

                                    html.P(
                                        [
                                            """
                                            This data categorise all products with various variation into a single group, 
                                            Unifying all difference. click
                                            """,
                                            html.Span("here", id = "open_grouped_modal", n_clicks = 0, className = "modal-link-style"),
                                            " for more information."
                                         ]
                                    ),

                                    dbc.Modal(
                                        [
                                            dbc.ModalHeader(dbc.ModalTitle("Grouped Product Data"), class_name = "modal-style"),
                                            dbc.ModalBody(
                                                dcc.Markdown(
                                                    """
                                                    The products are grouped in such a way that a single description is 
                                                    used for all variations.     
                                                    Example:    
                                                    The different types of berries such as *Blueberry*, *blackberry*, 
                                                    *strawberry*, etc, the name of the brand such as *purple berry plc*, 
                                                    *fresh-berries*, etc and other distinctive features such as size, 
                                                    price, quantity and so on are grouped into a unique product name 
                                                    called **'Berries'**.  
                                                    """
                                                ),
                                                class_name = "modal-style",
                                            ),
                                        ],
                                        id = "grouped_modal",
                                        is_open = False,
                                        centered = True,
                                    )
                                ],
                                className = "home-col-div",
                            ),
                       ],
                        class_name = "home-col",
                    ),


                    dbc.Col(
                        [
                            html.Div(
                                [
                                    html.H5("Taxonomy Product Data"),
                                    dbc.NavLink(
                                        [
                                            dbc.Button("USE DATA", id = "use_product_tax", n_clicks = 0)
                                        ],
                                        href = "/dashboard", active = "exact"
                                    ),

                                    html.Br(),

                                    html.P(
                                        [
                                            """
                                            This data differentiate products based on their characteristics.
                                            click here for more information. click
                                            """,
                                            html.Span("here", id = "open_tax_modal", n_clicks = 0, className = "modal-link-style"),
                                            " for more information.",
                                        ],
                                    ),

                                    dbc.Modal(
                                        [
                                            dbc.ModalHeader(dbc.ModalTitle("Taxonomy Product Data"), class_name = "modal-style"),
                                            dbc.ModalBody(
                                                dcc.Markdown(
                                                    """
                                                    Characteristics such as the product brand, price, type, size, 
                                                    quantity, style, etc are used to differentiate Each product
                                                    based on the stock-keeping Unit (SKU).
                                                
                                                    Then a product taxonomy is applied to the unique products. a taxonomy
                                                    in this case is an orderly hierarchy of items and items categories,
                                                    dividing things such that each item put into the basket analysis 
                                                    occurs with similar level of support. This is done by aggregating 
                                                    low-support items into groups and analyzing the group as a single
                                                    item.    
                                                        
                                                    Example: 
                                                    The following list of products with their support levels: 
                                                    - blueberry with 50% 
                                                    - blackberry with 45%  
                                                    - strawberry with 10%
                                                    - Raspberry with 15% 
                                                      
                                                    will be aggregated into:  
                                                    - blueberry 50%
                                                    - blackberry 45%
                                                    - berries (others) 25%  
                                                    
                                                    Another motivation for such arrangement is majorly for computational 
                                                    purpose. 
                                                    """
                                                ),
                                                class_name = "modal-style",
                                            ),
                                        ],
                                        id = "tax_modal",
                                        is_open = False,
                                        scrollable = True,
                                        centered = True,
                                    )
                                ],
                                className = "home-col-div",
                            )
                        ],
                        class_name = "home-col",

                    )
                ],
                class_name = "h-75",
                justify = "evenly"
            ),
        ],
        class_name = "home-container"
        ),
    ],
)


# Dashboard ============================================================================================================
dashboard_layout = html.Div(
    [
        html.Div(
            [
                html.Div([
                    dbc.NavbarSimple(
                        children = [
                            dbc.NavItem(dbc.NavLink("Home Page", href = "/"),),
                            dbc.NavItem(dbc.NavLink("Market Basket Analysis", href = "/mba"))
                        ],
                        brand = "Dashboard",
                        brand_href = "/dashboard",
                        color = "primary",
                        dark = True
                    ),
                ]),

                html.Div([
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    dbc.Card(
                                        dcc.Markdown(id = "n_transactions",),
                                        class_name = "dash-kpi-box"
                                    ),
                                ]
                            ),
                            dbc.Col(
                                [
                                    dbc.Card(
                                        dcc.Markdown(id = "n_unique_customers"),
                                        class_name = "dash-kpi-box"
                                    ),
                                ],
                            ),
                            dbc.Col(
                                [
                                    dbc.Card(
                                        dcc.Markdown(id = "total_sales"),
                                        class_name = "dash-kpi-box"
                                    ),
                                ],
                            ),
                            dbc.Col(
                                [
                                    dbc.Card(
                                        dcc.Markdown(id = "average_sales"),
                                        class_name = "dash-kpi-box"
                                    ),
                                ],
                            ),
                            dbc.Col(
                                [
                                    dbc.Card(
                                        dcc.Markdown(id = "n_unique_products"),
                                        class_name = "dash-kpi-box"
                                    ),
                                ],
                            ),
                        ],
                        justify = "between",
                        class_name = "dash-row-header"
                    )
                ]),

                html.Br(),

                html.Div([
                    dbc.Row(
                        [
                            dbc.Col( # Product Quantity -----------------------------------------|
                                [
                                    dbc.Card(
                                        [
                                            html.Div(
                                                [
                                                    comp_fun.db_setting_button(id = "collapse_product_quantity_settings"),

                                                    html.Br(),
                                                    html.Br(),

                                                    html.Div(
                                                        [
                                                            dbc.Collapse(
                                                                id = "collapse_product_quantity_content",
                                                                is_open = False,
                                                                children = [
                                                                    html.Label("Aggregate Type"),
                                                                    comp_fun.db_dcc_dropdown(id = "product_quantity_agg"),

                                                                    html.Br(),

                                                                    html.Label("Type Of Output"),
                                                                    comp_fun.db_dbc_radioitems(id = "product_quantity_output_type"),

                                                                    html.Br(),

                                                                    html.Label("Number Of Unique values"),
                                                                    comp_fun.db_dbc_num_input(id = "product_quantity_nunique"),
                                                                ],
                                                            )
                                                        ],
                                                        className = "dash-control"
                                                    )
                                                ]
                                            ),

                                            html.Div(id = "product_quantity_output"),
                                        ],
                                        class_name = "dash-display-box",
                                    )
                                ],
                                width = 6,
                            ),

                            dbc.Col( # Most purchase products -----------------------------------------------------|
                                [
                                    dbc.Card(
                                        [
                                            html.Div(
                                                [
                                                    comp_fun.db_setting_button(id = "collapse_purchase_product_settings"),

                                                    html.Br(),
                                                    html.Br(),

                                                    html.Div(
                                                        [
                                                            dbc.Collapse(
                                                                id = "collapse_purchase_product_content",
                                                                is_open = False,
                                                                children = [
                                                                    html.Label("Type Of Output"),
                                                                    comp_fun.db_dbc_radioitems(id = "purchase_product_output_type"),

                                                                    html.Br(),

                                                                    html.Label("Number Of Unique values"),
                                                                    comp_fun.db_dbc_num_input(id = "purchase_product_nunique"),
                                                                ],
                                                            ),
                                                        ],
                                                        className = "dash-control"
                                                    )
                                                ],
                                            ),

                                            html.Div(id = "product_purchase_output"),
                                        ],
                                        class_name = "dash-display-box"
                                    )
                                ],
                                width = 6,
                            ),
                        ],
                        # class_name = "dash-row-pt"
                    ),
                ]),

                html.Br(),

                html.Div([
                    dbc.Row(
                        [
                            dbc.Col( # Most Profitable Product. -------------------------------------------|
                                [
                                    dbc.Card(
                                        [
                                            comp_fun.db_setting_button(id = "collapse_profitable_product_settings"),

                                            html.Br(),
                                            html.Br(),

                                            html.Div(
                                                [
                                                    html.Div(
                                                        [
                                                            dbc.Collapse(
                                                                id = "collapse_profitable_product_content",
                                                                is_open = False,
                                                                children = [
                                                                    html.Label("Aggregate Type"),
                                                                    comp_fun.db_dcc_dropdown(id = "profitable_product_agg"),

                                                                    html.Br(),

                                                                    html.Label("Type Of Output"),
                                                                    comp_fun.db_dbc_radioitems(id = "profitable_product_output_type"),

                                                                    html.Br(),

                                                                    html.Label("Number Of Unique values"),
                                                                    comp_fun.db_dbc_num_input(id = "profitable_product_nunique"),
                                                                ],
                                                            )
                                                        ],
                                                        className = "dash-control-mw"
                                                    ),
                                                ]
                                            ),

                                            dcc.Loading(
                                                html.Div(id = "product_profitability_output"),
                                                id = "product_profitability_spinner",
                                                color = "white",
                                            ),
                                            html.Br(),
                                        ],
                                        class_name = "dash-display-box",
                                    ),
                                ],
                            ),
                        ],
                        # class_name = "dash-row-pt"
                    ),
                ], className = "dash-display-wide")
            ],
            className = "dash-container",
        ),
    ],
)

# MBA Analysis =========================================================================================================
run_mba_analysis = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.Label("Minimum Support",),
                                dbc.Input(
                                    id = "min_support",
                                    type = "number",
                                    min = 0.0001, max = 0.009, step = 0.0001,
                                    value = 0.005,
                                    class_name = "dash-control-bc",
                                    persistence = True,
                                    persistence_type = "memory",
                                ),
                                dbc.Tooltip(
                                    """Filter out items with <= the input support. must be between 0 and 1""",
                                    target = "min_support",
                                    placement = "top",
                                    delay = {"hide": 100}
                                ),

                                html.Br(),

                                html.Label("Maximum Length",),
                                dbc.Input(
                                    id = "max_length",
                                    type = "number",
                                    min = 1,
                                    class_name = "dash-control-bc",
                                    persistence = True,
                                    persistence_type = "memory",
                                ),
                                dbc.Tooltip(
                                    """
                                    Maximum length of the itemsets generated. If empty all possible itemsets  are
                                    evaluated.
                                    """,
                                    target = "max_length",
                                    placement = "right",
                                    delay = {"hide": 200}
                                ),

                                html.Br(),

                                html.Label("Metric Rule",),
                                dcc.Dropdown(
                                    id = "rule_metric",
                                    options = [
                                        {"label": str.title(rule), "value": rule} for rule in ["support", "confidence", "lift", "leverage", "conviction"]
                                    ],
                                    value = "lift",
                                    searchable = True,
                                    persistence = True,
                                    persistence_type = "memory",
                                ),
                                dbc.Tooltip(
                                    """
                                    Metric to evaluate if a rule is of interest.
                                    """,
                                    target = "rule_metric",
                                    placement = "right",
                                    delay = {"hide": 100}
                                ),

                                html.Br(),

                                html.Label("Minimum Threshold",),
                                dbc.Input(
                                    id = "min_threshold",
                                    type = "number",
                                    class_name = "dash-control-bc",
                                    persistence = True,
                                    persistence_type = "memory",
                                ),
                                dbc.Tooltip(
                                    """
                                    Minimal threshold for the evaluation metric, via the `Metric Rule` value, to decide 
                                    whether a candidate rule is of interest.
                                    """,
                                    target = "min_threshold",
                                    placement = "right",
                                    delay = {"hide": 200}
                                ),

                                html.Br(),

                                html.Label("Type Of Output",),
                                dbc.RadioItems(
                                    id = "mba_analysis_output_type",
                                    options = [
                                        {"label": "Rules", "value": "rules"},
                                        {"label": "Support Length", "value": "sup_len"},
                                    ],
                                    value = "rules",
                                    input_class_name = "dash-control-bc",
                                    persistence = True,
                                    persistence_type = "memory",
                                ),

                                html.Br(),

                                html.Div(
                                    [
                                        dbc.Button(
                                            id = "create_mba_rules",
                                            children = "Create",
                                            n_clicks = 0,
                                            color = "success",
                                            class_name = "me-1"
                                        ),
                                    ],
                                    className = "d-grid gap-2",
                                ),
                            ],
                            className = "mba-sidebar"
                        ),
                    ],
                    width = 3,
                    class_name = "align-text-left label-color",
                ),

                dbc.Col(
                    [
                        html.Div(
                            dbc.Card(
                                dcc.Loading(
                                    html.Div(id = "mba_analysis_output",),
                                    id = "mba_analysis_spinner",
                                    color = "white",
                                )
                            ),
                        ),

                        html.Br(),

                        html.Div(
                            dcc.Markdown(
                                id = "mba_analysis_table_description"
                            ),
                            className = "description-div",
                        ),
                    ],
                    width = 9,
                ),
            ],
        ),
    ],
    fluid = True,
    class_name = "container-top-padding",
)

wangle_mba_rules = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                comp_fun.filter_div(id_type = "jq"),

                                html.Br(),

                                dbc.Card(
                                    [
                                        html.Label("X Variable"),
                                        comp_fun.rel_dcc_dropdown(id = "x_variable"),

                                        html.Br(),

                                        html.Label("Y Variable"),
                                        comp_fun.rel_dcc_dropdown(id = "y_variable"),

                                        html.Br(),

                                        html.Label("Z Variable (Optional)"),
                                        comp_fun.rel_dcc_dropdown(id = "z_variable"),

                                        html.Br(),

                                        html.Label("Opacity (Optional)"),
                                        dbc.Input(
                                            id = "rel_plt_opacity",
                                            type = "number",
                                            min = 0, max = 1,
                                            persistence = True,
                                            persistence_type = "memory",
                                        ),

                                        html.Br(),

                                        dbc.Button(
                                            children = "Create Plot",
                                            id = "create_rel_plot",
                                            n_clicks = 0,
                                            size = "lg",
                                            color = "success",
                                            class_name = "me-1",
                                        )
                                    ],
                                    class_name = "content-padding acd-bg",
                                ),
                            ],
                            className = "acd-bg",
                        ),
                    ],
                    width = 3,
                    class_name = "align-text-left"
                ),

                dbc.Col(
                    [
                        html.Div(
                            dbc.Card(
                                dcc.Loading(
                                    html.Div(id = "mba_query_output", ),
                                    id = "mba_query_spinner",
                                    color = "white",
                                ),
                            ),
                        ),

                        html.Div(
                            dcc.Markdown(
                                id = "mba_query_table_description"
                            ),
                            className = "description-div",
                        ),

                        html.Br(),

                        html.Div(
                            dbc.Card(
                                dcc.Loading(
                                    html.Div(id = "metric_relationship_plot", ),
                                    id = "metric_rel_spinner",
                                    color = "white",
                                ),
                            ),
                        )
                    ],
                    width = 9,
                ),
            ],
            class_name = "board-color",
        ),
    ],
    fluid = True,
    class_name = "container-top-padding",
)

mba_analysis_layout = html.Div(
    [
        html.Div([
            dbc.NavbarSimple(
                children = [
                    dbc.NavItem(dbc.NavLink("Home Page", href = "/")),
                    dbc.NavItem(dbc.NavLink("Dashboard", href = "/dashboard")),
                    dbc.NavItem(dbc.NavLink("Assign Products", href = "/assign-products")),
                ],
                brand = "Market Basket Analysis",
                brand_href = "/mba",
                color = "primary",
                dark = True
            ),
        ]),

        dbc.Tabs(
            [
                dbc.Tab(
                    run_mba_analysis,
                    label = "Market Basket Analysis",
                    tab_class_name = "tab-inactive-style",
                    label_class_name = "label-inactive-style",
                    active_tab_class_name = "tab-active-style",
                    active_label_class_name = "label-active-style",
                ),
                dbc.Tab(
                    wangle_mba_rules,
                    label = "View Rules",
                    tab_class_name = "tab-inactive-style",
                    label_class_name = "label-inactive-style",
                    active_tab_class_name = "tab-active-style",
                    active_label_class_name = "label-active-style",
                ),
            ],
            persistence = True,
            persistence_type = "memory",
        )
    ],
)


# Get likely Products ==================================================================================================
get_likely_products = html.Div(
    [
        html.Div([
            dbc.NavbarSimple(
                children = [
                    dbc.NavItem(dbc.NavLink("Home Page", href = "/")),
                    dbc.NavItem(dbc.NavLink("Dashboard", href = "/dashboard")),
                    dbc.NavItem(dbc.NavLink("Market Basket Analysis", href = "/mba")),
                ],
                brand = "Assign Products",
                brand_href = "/assign-products",
                color = "primary",
                dark = True
            ),
        ]),

        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                comp_fun.filter_div(id_type = "gl"),

                                dbc.Card(
                                    [
                                       html.Br(),

                                       dbc.InputGroup(
                                           [
                                               dbc.InputGroupText("Number of Rules", class_name = "acd-bg"),
                                               dbc.Input(
                                                   id = "rule_range",
                                                   type = "number",
                                                   min = 1, max = 10, step = 1,
                                                   value = 1,
                                                   class_name = "dash-control-bc",
                                                   persistence = True,
                                                   persistence_type = "memory",
                                               ),
                                           ],
                                       ),

                                       html.Br(),

                                       html.Label("Extraction Arrangement"),
                                       dbc.RadioItems(
                                           id = "rule_arrangement",
                                           options = [
                                              {"label": "Combine Itemset", "value": False},
                                              {"label": "Distinct Itemset", "value": True},
                                           ],
                                           value = False,
                                           input_class_name = "dash-control-bc",
                                           persistence = True,
                                           persistence_type = "memory",
                                      ),

                                      html.Br(),

                                      html.Label("Create"),
                                      dbc.RadioButton(
                                          id = "just_customer_id",
                                          label = "Just Customer IDs",
                                          input_class_name = "dash-control-bc",
                                      ),

                                      html.Br(),
                                      html.Br(),

                                      html.Div(
                                          [
                                              dbc.Button(
                                                  id = "create_likely_purchase_products",
                                                  children = "Assign",
                                                  n_clicks = 0,
                                                  size = "lg",
                                                  color = "success",
                                                  class_name = "me-1",
                                              ),
                                          ],
                                          className = "d-grid gap-2",
                                      )
                                    ],
                                    class_name = "content-padding acd-bg",
                                ),
                            ],
                            className = "acd-bg",
                        ),
                    ],
                    width = 3,
                    class_name = "align-text-left",
                ),

                dbc.Col(
                    [
                        dbc.Card(
                            [
                                html.Div(id = "filtered_rules_for_extraction", className = "mba-main-content",),
                            ]
                        ),

                        html.Div(
                            dcc.Markdown(
                                id = "mba_filtered_rules_table_description"
                            ),
                            className = "description-div",
                        ),

                        html.Br(),
                        html.Br(),

                        dbc.Card(
                            [
                                html.Div(id = "likely_product_purchase_output", className = "mba-main-content",),
                            ]
                        )
                    ],
                    width = 9,
                ),
            ],
        ),
    ],
)


# Layout ===============================================================================================================
app.layout = html.Div(
    html.Div(
        [
            dcc.Location(id = "url"),
            dbc.Nav(
                [
                    dbc.NavItem(
                        id = "current_page",
                        children = [],
                    ),
                ],
                fill = True,
            ),
            html.Div(
                [
                    dcc.Store(id = "store_data"),
                    dcc.Store(id = "store_rule_data"),
                    dcc.Store(id = "filter_rule_data"),
                ],
            ),
        ],
    ),
)

# Callback =============================================================================================================

@app.callback( Output("current_page", "children"), Input("url", "pathname"),)
def render_page_content(pathname):
    if pathname == "/":
        return home_content
    elif pathname == "/dashboard":
        return dashboard_layout
    elif pathname == "/mba":
        return mba_analysis_layout
    elif pathname == "/assign-products":
        return get_likely_products


@app.callback(
    Output("grouped_modal", "is_open"),
    Input("open_grouped_modal", "n_clicks"),
    State("grouped_modal", "is_open"),
)
def toggle_grouped_modal(open_click,  is_open):
    if open_click:
        return not is_open
    return is_open

@app.callback(
    Output("tax_modal", "is_open"),
    Input("open_tax_modal", "n_clicks"),
    State("tax_modal", "is_open"),
)
def toggle_grouped_modal(open_click,  is_open):
    if open_click:
        return not is_open
    return is_open



@app.callback( Output("store_data", "data"), Input("use_product", "n_clicks"), Input("use_product_tax", "n_clicks"),)
def update_data_choice(use_grouped_products, use_products_tax):
    if use_grouped_products and use_products_tax == 0:
        return trans_df.to_json(date_format = "iso", orient = "split")

    elif use_grouped_products == 0 and use_products_tax > 0:
        prod_tax = mba_fun.make_Product_Taxonomy(df = trans_df, threshold = 60)
        return prod_tax.to_json(date_format = "iso", orient = "split")

    elif use_grouped_products and use_products_tax:
        if ctx.triggered_id is not None:
            button_id = ctx.triggered_id

            if button_id == "use_product":
                return trans_df.to_json(date_format="iso", orient="split")
            elif button_id == "use_product_tax":
                prod_tax = mba_fun.make_Product_Taxonomy(df = trans_df, threshold=60)
                return prod_tax.to_json(date_format="iso", orient="split")
    else:
        dash.no_update



@app.callback(
    Output("collapse_product_quantity_content", "is_open"),
    Input("collapse_product_quantity_settings", "n_clicks"),
    State("collapse_product_quantity_content", "is_open")
)
def toggle_collapse_qty(n, is_open):
    return comp_fun.toggle_plot_setting(n, is_open)

@app.callback(
    Output("collapse_purchase_product_content", "is_open"),
    Input("collapse_purchase_product_settings", "n_clicks"),
    State("collapse_purchase_product_content", "is_open")
)
def toggle_collapse_product(n, is_open):
    return comp_fun.toggle_plot_setting(n, is_open)

@app.callback(
    Output("collapse_profitable_product_content", "is_open"),
    Input("collapse_profitable_product_settings", "n_clicks"),
    State("collapse_profitable_product_content", "is_open")
)
def toggle_collapse_profitable(n, is_open):
    return comp_fun.toggle_plot_setting(n, is_open)


@app.callback(
    Output("n_transactions", "children"),
    Output("n_unique_customers", "children"),
    Output("total_sales", "children"),
    Output("average_sales", "children"),
    Output("n_unique_products", "children"),
    Input("store_data", "data"),
)
def update_no_transaction(jsonified_data):
    if jsonified_data is not None:
        trans_tbl = pd.read_json(jsonified_data, orient = "split")

        n_trasactions = mba_fun.create_data_info(df = trans_tbl, info_type = "no_transaction")
        n_trasactions_output = f"""
                                Number Of Transactions  
                                **{n_trasactions:,}**
                                """

        n_unique_customers = mba_fun.create_data_info(df = trans_tbl, info_type = "no_unique_customers")
        n_unique_customers_output = f"""
                                     Number Of Unique Customer  
                                     **{n_unique_customers:,}**
                                     """

        total_sales = mba_fun.create_data_info(df = trans_tbl, info_type = "total_sales")
        total_sales_out = f"""
                           Total Product Sales  
                           **{total_sales:,.2f}**
                           """

        average_sales = mba_fun.create_data_info(df = trans_tbl, info_type = "average_sales")
        average_sales_out = f"""
                             Average Product Sales  
                             **{average_sales:,.2f}**
                             """

        n_unique_products = mba_fun.create_data_info(df = trans_tbl, info_type = "unique_products")
        n_unique_products_out = f"""
                                 Number Of Unique Product  
                                 **{n_unique_products:,}**
                                 """

        return n_trasactions_output, n_unique_customers_output, total_sales_out, average_sales_out, n_unique_products_out
    else:
        def no_output(value_type):
            return f"""
                    **{value_type}**  
                    Updating....
                    """
        return (no_output("Number Of Transcations"), no_output("Number Of Unique Customers"),
                no_output("Total Product Sales"), no_output("Average Product Sales"), no_output("Number Of Unique Product"))


@app.callback(
    Output("product_quantity_output", "children"),
    Input("store_data", "data"),
    Input("product_quantity_agg", "value"),
    Input("product_quantity_output_type", "value"),
    Input("product_quantity_nunique", "value"),
)
def update_product_quantity_output(jsonified_data, agg_fun, output_type, n_unique):
    if jsonified_data is not None:
        trans_tbl = pd.read_json(jsonified_data, orient = "split")

        f_output = mba_fun.product_quantity(df = trans_tbl, agg_function = agg_fun, output_type = output_type, max_unique_value = n_unique)

        if output_type == "plot":
            return comp_fun.create_graph(f_output)
        elif output_type == "table":
            return comp_fun.create_dataframe(df = f_output, page_size = 13)
    else:
        return dash.no_update

@app.callback(
    Output("product_purchase_output", "children"),
    Input("store_data", "data"),
    Input("purchase_product_output_type", "value"),
    Input("purchase_product_nunique", "value"),
)
def update_product_purchase_output(jsonified_data, output_type, n_unique):
    if jsonified_data is not None:
        trans_tbl = pd.read_json(jsonified_data, orient = "split")

        f_output = mba_fun.most_purchased_products(df = trans_tbl, output_type = output_type, max_unique_value = n_unique)

        if output_type == "plot":
            return comp_fun.create_graph(f_output)
        elif output_type == "table":
            return comp_fun.create_dataframe(df = f_output, page_size = 13)
    else:
        return dash.no_update

@app.callback(
    Output("product_profitability_output", "children"),
    Input("store_data", "data"),
    Input("profitable_product_agg", "value"),
    Input("profitable_product_output_type", "value"),
    Input("profitable_product_nunique", "value"),
)
def update_product_profitability_output(jsonified_data, agg_fun, output_type, n_unique):
    if jsonified_data is not None:
        trans_tbl = pd.read_json(jsonified_data, orient = "split")

        f_output = mba_fun.most_profitable_product(df = trans_tbl, agg_function = agg_fun, output_type = output_type, max_unique_value = n_unique)

        if output_type == "plot":
            return comp_fun.create_graph(f_output)
        elif output_type == "table":
            return html.P("There is a problem with this output as a result of dash.data_table issues")
            # return comp_fun.create_dataframe(df = f_output, page_size = 15)
    else:
        return dash.no_update



@app.callback(
    Output("min_threshold", "min"),
    Output("min_threshold", "max"),
    Output("min_threshold", "value"),
    Input("rule_metric", "value"),
)
def create_min_threshold_value(matric):
    if matric == "support":
        return 0, 1, 0.005
    elif matric == "confidence":
        return 0, 1, 0.01
    elif matric == "lift":
        return 0, 10, 1
    elif matric == "leverage":
        return -1, 1, 0.001
    elif matric == "conviction":
        return 0, 10, 1
    else:
        dash.no_update

@app.callback(
    Output("mba_analysis_output", "children"),
    Output("mba_analysis_table_description", "children"),
    Output("store_rule_data", "data"),

    Input("store_data", "data"),
    Input("create_mba_rules", "n_clicks"),

    State("min_support", "value"),
    State("max_length", "value"),
    State("rule_metric", "value"),
    State("min_threshold", "value"),
    State("mba_analysis_output_type", "value"),
)
def create_mba_rules(jsonified_data, n_click, min_support, max_len, rule_metric, min_threshold, mba_analysis_output_type):
    if jsonified_data is not None:
        trans_tbl = pd.read_json(jsonified_data, orient = "split")

        try:
            if n_click:
                mba_rules = mba_fun.create_association_rule(df = trans_tbl,
                                                            min_support = min_support,
                                                            max_length = max_len,
                                                            rule_metric = rule_metric,
                                                            min_threshold = min_threshold,
                                                            output_type = mba_analysis_output_type)

                description = mba_fun.metric_description(df = mba_rules, return_type = mba_analysis_output_type)

                if mba_analysis_output_type == "rules":
                    mba_rules_out = mba_fun.str_frozenset(df = mba_rules, df_type = "with_rules")

                elif mba_analysis_output_type == "sup_len":
                    mba_rules_out = mba_fun.str_frozenset(df = mba_rules, df_type = "sup_len")

                    # To always return a rule table for filtering ----------------------------------|
                    mba_rules = mba_fun.create_association_rule(df = trans_tbl,
                                                                min_support = min_support,
                                                                max_length = max_len,
                                                                rule_metric = rule_metric,
                                                                min_threshold = min_threshold,
                                                                output_type = "rules")

                child_output = comp_fun.create_dataframe(df = mba_rules_out, page_size = 20, precision = 4)
                desc_output = comp_fun.create_description_table(m_dict = description,
                                                                return_type = mba_analysis_output_type,
                                                                return_name = "Analysis")

                return child_output, desc_output, mba_rules.to_json(date_format = "iso", orient = "split")
            else:
                raise dash.exceptions.PreventUpdate
        except:
            return dash.no_update, dash.no_update, dash.no_update
    else:
        return dash.no_update, dash.no_update, dash.no_update



@app.callback(Output("jq_f_product_type", "options"), Output("jq_s_product_type", "options"), Input("store_data", "data"), )
def update_unique_products(jsonified_data):
    if jsonified_data is not None:
        trans_tbl = pd.read_json(jsonified_data, orient = "split")

        unique_products = mba_fun.unique_products(df = trans_tbl)

        return unique_products, unique_products
    else:
        dash.no_update, dash.no_update


@app.callback(
    Output("jq_query_dynamic_divs", "children"),

    Input("jq_support_add", "n_clicks"),
    Input("jq_confidence_add", "n_clicks"),
    Input("jq_lift_add", "n_clicks"),
    Input("jq_leverage_add", "n_clicks"),
    Input("jq_conviction_add", "n_clicks"),
    Input("jq_ant_support_add", "n_clicks"),
    Input("jq_con_support_add", "n_clicks"),

    Input({"type": "jq_support_del_btn", "index": ALL}, "n_clicks"),
    Input({"type": "jq_confidence_del_btn", "index": ALL}, "n_clicks"),
    Input({"type": "jq_lift_del_btn", "index": ALL}, "n_clicks"),
    Input({"type": "jq_leverage_del_btn", "index": ALL}, "n_clicks"),
    Input({"type": "jq_conviction_del_btn", "index": ALL}, "n_clicks"),
    Input({"type": "jq_ant_support_del_btn", "index": ALL}, "n_clicks"),
    Input({"type": "jq_con_support_del_btn", "index": ALL}, "n_clicks"),

    State("jq_query_dynamic_divs", "children")
)
def add_query_div(support_cls, confidence_cls, lift_cls, leverage_cls, conviction_cls, ant_support_cls, con_support_cls,
                  support_del_cls, confidence_del_cls, lift_del_cls, leverage_del_cls, conviction_del_cls, ant_support_del_cls, con_support_del_cls,
                  div_children):
    return comp_fun.add_filter_div(id_type = "jq", children_div = div_children)



@app.callback( Output("jq_f_rule_type", "options"), Input("jq_s_rule_type", "value") )
def disable_frule_type(opts):
    return comp_fun.disable_fs_rule_type(opts, typ = "single")

@app.callback( Output("jq_s_rule_type", "options"), Input("jq_f_rule_type", "value") )
def disable_srule_type(opts):
    return comp_fun.disable_fs_rule_type(opts, typ = "single")


@app.callback(
    Output("mba_query_output", "children"),
    Output("mba_query_table_description", "children"),

    Input("store_rule_data", "data"),

    Input("jq_filter_rule_contain_products", "n_clicks"),
    State("jq_f_rule_type", "value"),
    State("jq_f_product_type", "value"),
    State("jq_contains_bitwise_opt", "value"),
    State("jq_s_rule_type", "value"),
    State("jq_s_product_type", "value"),
    State("jq_contains_search_type", "value"),

    Input("jq_filter_rule_query_metrics", "n_clicks"),
    State({"type": "jq_input_label", "index": ALL}, "children"),
    State({"type": "jq_value", "index": ALL}, "value"),
    State({"type": "jq_comparison_opt", "index": ALL}, "value"),
    State({"type": "jq_bitwise_opt", "index": ALL}, "value"),

    Input("jq_filter_rule_rule_length", "n_clicks"),
    State("jq_len_rule_metric_type", "value"),
    State("jq_rule_length_comp_opt", "value"),
    State("jq_length_products", "value"),
)
def filter_view_rules(jsonified_data, ct_click, ct_f_rule_type, ct_f_product_type, ct_bitwise_opt, ct_s_rule_type, ct_s_product_type, ct_search_type,
                      q_matric_click, q_matric_input_label, q_matric_input, q_matric_comp_opt, q_matric_bitwise_opt,
                      len_click, len_matric_type, len_comp_opt, len_n_product,):

    if jsonified_data is not None:
        trans_tbl = pd.read_json(jsonified_data, orient = "split")
        trans_tbl = mba_fun.freeze_set(trans_tbl)

        if ctx.triggered_id is not None:
            button_id = ctx.triggered_id

            if ct_click and button_id == "jq_filter_rule_contain_products":
                filtered_rules = mba_fun.filter_products_contain(df = trans_tbl,
                                                                 search_type = ct_search_type,
                                                                 f_rule_type = ct_f_rule_type, f_product_type = ct_f_product_type,
                                                                 s_rule_type = ct_s_rule_type, s_product_type = ct_s_product_type,
                                                                 bitwise_opt = ct_bitwise_opt)

            elif q_matric_click and button_id == "jq_filter_rule_query_metrics":
                cleaned_values = mba_fun.get_query_values(metric = q_matric_input_label,
                                                          metric_value = q_matric_input,
                                                          comp_op = q_matric_comp_opt,
                                                          bitw_op = q_matric_bitwise_opt)

                filtered_rules = mba_fun.filter_rules_values(df = trans_tbl,
                                                             query_values = cleaned_values[0],
                                                             comp_op = cleaned_values[1],
                                                             bitw_op = cleaned_values[2])

            elif len_click and button_id == "jq_filter_rule_rule_length":
                filtered_rules = mba_fun.filter_rules_length(df = trans_tbl,
                                                             rule_type = len_matric_type,
                                                             comp_op = len_comp_opt,
                                                             length = len_n_product)

            try:
                if button_id in ["jq_filter_rule_contain_products", "jq_filter_rule_query_metrics", "jq_filter_rule_rule_length"]:
                    description = mba_fun.metric_description(df = filtered_rules, return_type = "rules")
                    unfreez_filtered_rules = mba_fun.str_frozenset(df = filtered_rules)

                    filtered_output = comp_fun.create_dataframe(df = unfreez_filtered_rules, page_size = 20, precision = 4)
                    desc_output = comp_fun.create_description_table(m_dict = description, return_type = "rules", return_name = "Filtered Data")

                    return filtered_output, desc_output
                else:
                    return dash.no_update, dash.no_update
            except:
                return dash.no_update, dash.no_update
    else:
        return dash.no_update, dash.no_update


@app.callback( Output("x_variable", "options"), Input("y_variable", "value"), Input("z_variable", "value") )
def disable_variable_option(y_var, z_var):
    return comp_fun.disable_fs_rule_type(y_var, z_var, typ = "double")

@app.callback( Output("y_variable", "options"), Input("x_variable", "value"), Input("z_variable", "value") )
def disable_variable_option(x_var, z_var):
    return comp_fun.disable_fs_rule_type(x_var, z_var, typ = "double")

@app.callback( Output("z_variable", "options"), Input("x_variable", "value"), Input("y_variable", "value") )
def disable_variable_option(x_var, y_var):
    return comp_fun.disable_fs_rule_type(x_var, y_var, typ = "double")


@app.callback(
    Output("metric_relationship_plot", "children"),

    Input("store_rule_data", "data"),
    Input("create_rel_plot", "n_clicks"),
    State("x_variable", "value"),
    State("y_variable", "value"),
    State("z_variable", "value"),
    State("rel_plt_opacity", "value"),
)
def update_rel_plot(jsonified_data, plt_click, x_var, y_var, z_var, opacity):
    if jsonified_data is not None:
        trans_tbl = pd.read_json(jsonified_data, orient = "split")
        trans_tbl = mba_fun.freeze_set(trans_tbl)

        if plt_click:
            rel_output = mba_fun.rules_relationship(df = trans_tbl, x_var = x_var, y_var = y_var, z_var = z_var, opacity = opacity)

            return comp_fun.create_graph(rel_output)
        else:
            return dash.no_update
    else:
        return dash.no_update



@app.callback(Output("gl_f_product_type", "options"), Output("gl_s_product_type", "options"), Input("store_data", "data"),)
def update_unique_products(jsonified_data):
    if jsonified_data is not None:
        trans_tbl = pd.read_json(jsonified_data, orient = "split")

        unique_products = mba_fun.unique_products(df = trans_tbl)

        return unique_products, unique_products
    else:
        dash.no_update, dash.no_update




@app.callback(
    Output("gl_query_dynamic_divs", "children"),

    Input("gl_support_add", "n_clicks"),
    Input("gl_confidence_add", "n_clicks"),
    Input("gl_lift_add", "n_clicks"),
    Input("gl_leverage_add", "n_clicks"),
    Input("gl_conviction_add", "n_clicks"),
    Input("gl_ant_support_add", "n_clicks"),
    Input("gl_con_support_add", "n_clicks"),

    Input({"type": "gl_support_del_btn", "index": ALL}, "n_clicks"),
    Input({"type": "gl_confidence_del_btn", "index": ALL}, "n_clicks"),
    Input({"type": "gl_lift_del_btn", "index": ALL}, "n_clicks"),
    Input({"type": "gl_leverage_del_btn", "index": ALL}, "n_clicks"),
    Input({"type": "gl_conviction_del_btn", "index": ALL}, "n_clicks"),
    Input({"type": "gl_ant_support_del_btn", "index": ALL}, "n_clicks"),
    Input({"type": "gl_con_support_del_btn", "index": ALL}, "n_clicks"),

    State("gl_query_dynamic_divs", "children")
)
def add_query_div(support_cls, confidence_cls, lift_cls, leverage_cls, conviction_cls, ant_support_cls, con_support_cls,
                  support_del_cls, confidence_del_cls, lift_del_cls, leverage_del_cls, conviction_del_cls, ant_support_del_cls, con_support_del_cls,
                  div_children):
    return comp_fun.add_filter_div(id_type = "gl", children_div = div_children)


@app.callback( Output("gl_f_rule_type", "options"), Input("gl_s_rule_type", "value") )
def disable_frule_type(opts):
    return comp_fun.disable_fs_rule_type(opts, typ = "single")

@app.callback( Output("gl_s_rule_type", "options"), Input("gl_f_rule_type", "value") )
def disable_srule_type(opts):
    return comp_fun.disable_fs_rule_type(opts, typ = "single")


@app.callback(
    Output("filtered_rules_for_extraction", "children"),
    Output("mba_filtered_rules_table_description", "children"),
    Output("filter_rule_data", "data"),

    Input("store_rule_data", "data"),

    Input("gl_filter_rule_contain_products", "n_clicks"),
    State("gl_f_rule_type", "value"),
    State("gl_f_product_type", "value"),
    State("gl_contains_bitwise_opt", "value"),
    State("gl_s_rule_type", "value"),
    State("gl_s_product_type", "value"),
    State("gl_contains_search_type", "value"),

    Input("gl_filter_rule_query_metrics", "n_clicks"),
    State({"type": "gl_input_label", "index": ALL}, "children"),
    State({"type": "gl_value", "index": ALL}, "value"),
    State({"type": "gl_comparison_opt", "index": ALL}, "value"),
    State({"type": "gl_bitwise_opt", "index": ALL}, "value"),

    Input("gl_filter_rule_rule_length", "n_clicks"),
    State("gl_len_rule_metric_type", "value"),
    State("gl_rule_length_comp_opt", "value"),
    State("gl_length_products", "value"),
)
def filter_rules(jsonified_rule_data,
                 ct_click, ct_f_rule_type, ct_f_product_type, ct_bitwise_opt, ct_s_rule_type, ct_s_product_type, ct_search_type,
                 q_matric_click, q_matric_input_label, q_matric_input, q_matric_comp_opt, q_matric_bitwise_opt,
                 len_click, len_matric_type, len_comp_opt, len_n_product):

    if jsonified_rule_data is not None:
        trans_rule_tbl = pd.read_json(jsonified_rule_data, orient = "split")
        trans_rule_tbl = mba_fun.freeze_set(trans_rule_tbl)

        if ctx.triggered_id is not None:
            button_id = ctx.triggered_id

            if ct_click and button_id == "gl_filter_rule_contain_products":
                filtered_rules = mba_fun.filter_products_contain(df = trans_rule_tbl,
                                                                 search_type = ct_search_type,
                                                                 f_rule_type = ct_f_rule_type, f_product_type = ct_f_product_type,
                                                                 s_rule_type = ct_s_rule_type, s_product_type = ct_s_product_type,
                                                                 bitwise_opt = ct_bitwise_opt)

            elif q_matric_click and button_id == "gl_filter_rule_query_metrics":
                cleaned_values = mba_fun.get_query_values(metric = q_matric_input_label,
                                                          metric_value = q_matric_input,
                                                          comp_op = q_matric_comp_opt,
                                                          bitw_op = q_matric_bitwise_opt)

                filtered_rules = mba_fun.filter_rules_values(df = trans_rule_tbl,
                                                             query_values = cleaned_values[0],
                                                             comp_op = cleaned_values[1],
                                                             bitw_op = cleaned_values[2])

            elif len_click and button_id == "gl_filter_rule_rule_length":
                filtered_rules = mba_fun.filter_rules_length(df = trans_rule_tbl,
                                                             rule_type = len_matric_type,
                                                             comp_op = len_comp_opt,
                                                             length = len_n_product)

            try:
                if button_id in ["gl_filter_rule_contain_products", "gl_filter_rule_query_metrics", "gl_filter_rule_rule_length"]:
                    description = mba_fun.metric_description(df = filtered_rules, return_type = "rules")
                    unfreez_filtered_rules = mba_fun.str_frozenset(df = filtered_rules)

                    filtered_output = comp_fun.create_dataframe(df = unfreez_filtered_rules, page_size = 20, precision = 4)
                    desc_output = comp_fun.create_description_table(m_dict = description, return_type = "rules", return_name = "Filtered Data")

                    return filtered_output, desc_output, filtered_rules.to_json(date_format = "iso", orient = "split")
                else:
                    return dash.no_update, dash.no_update, dash.no_update
            except:
                return dash.no_update, dash.no_update, dash.no_update
    else:
        return dash.no_update, dash.no_update, dash.no_update


@app.callback(
    Output("likely_product_purchase_output", "children"),

    Input("store_data", "data"),
    Input("store_rule_data", "data"),
    Input("filter_rule_data", "data"),

    Input("create_likely_purchase_products", "n_clicks"),
    State("rule_range", "value"),
    State("rule_arrangement", "value"),
    State("just_customer_id", "value"),
)
def create_likely_purchase_products(jsonified_data, rule_jsonified_data, filter_rule_jsonified_data,
                                    likely_click, range_rules, arrangement, just_id):

    if jsonified_data is not None and rule_jsonified_data is not None:
        trans_tbl = pd.read_json(jsonified_data, orient = "split")
        rule_tbl = pd.read_json(rule_jsonified_data, orient = "split")

        if filter_rule_jsonified_data is not None:
            selected_rule_tbl = pd.read_json(filter_rule_jsonified_data, orient = "split")
        else:
            selected_rule_tbl = rule_tbl


        if likely_click:
            selected_rule_tbl = mba_fun.freeze_set(selected_rule_tbl)
            selected_filtered_rules = mba_fun.unfreez_set(df = selected_rule_tbl)

            ant_products = mba_fun.extract_product_rules(df = selected_filtered_rules,
                                                         rule_type = "antecedents",
                                                         rule_range = range_rules,
                                                         by_row = arrangement)

            con_products = mba_fun.extract_product_rules(df = selected_filtered_rules,
                                                         rule_type = "consequents",
                                                         rule_range = range_rules,
                                                         by_row = arrangement)

            likely_product_output = mba_fun.protential_customer_product(df = trans_tbl,
                                                                        ant_products = ant_products,
                                                                        con_products = con_products,
                                                                        just_customer_id = just_id,
                                                                        distinct_product_group = arrangement)

            return comp_fun.create_dataframe(df = likely_product_output, page_size = 20, precision = 1)


if __name__ == "__main__":
    app.run_server(debug = True)



