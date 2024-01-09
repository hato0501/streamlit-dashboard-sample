import streamlit as st
import streamlit_shadcn_ui as ui
import pandas as pd
from datetime import datetime, timezone, timedelta

import numpy as np
import plotly.figure_factory as ff
import streamlit_antd_components as sac

import plotly.graph_objects as go


st.set_page_config(
    page_title="hammock Cockpit for ENEOS-VPP", page_icon="✈️", layout="wide"
)


with open("static/style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

with st.sidebar:
    menu = sac.menu(
        index=1,
        items=[
            sac.MenuItem(
                "monitor",
                icon="display",
                children=[
                    sac.MenuItem("dashboard", icon="eye"),
                    sac.MenuItem(
                        "downloads",
                        icon="download",
                    ),
                ],
            ),
            sac.MenuItem(
                "simulator",
                icon="clock",
            ),
            sac.MenuItem(
                "VPP Settings",
                icon="gear",
                children=[
                    sac.MenuItem("Resources", icon="battery"),
                    sac.MenuItem(
                        "Trading",
                        icon="graph-up",
                    ),
                ],
            ),
            sac.MenuItem(type="divider"),
            sac.MenuItem(
                "link",
                # type="group",
                children=[
                    sac.MenuItem(
                        "antd-menu",
                        icon="heart-fill",
                        href="https://ant.design/components/menu#menu",
                    ),
                    sac.MenuItem(
                        "bootstrap-icon",
                        icon="bootstrap-fill",
                        href="https://icons.getbootstrap.com/",
                    ),
                ],
            ),
        ],
        format_func="title",
        size="sm",
        variant="filled",
        indent=10,
        open_all=True,
    )


def get_summary():
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("年度粗利進捗", expanded=True):
            fiscal_year = st.selectbox(
                "年度",
                [
                    "FY2023",
                ],
            )
            subcol1, subcol2, subcol3 = st.columns(3)
            with subcol1:
                st.metric(
                    "粗利実績 (年度合計)",
                    "1.3 億円",
                )
            with subcol2:
                st.metric(
                    "通期目標",
                    "5.1 億円",
                )
            with subcol3:
                st.metric(
                    "通期進捗率",
                    f"{1.3/5.1*100:.1f}%",
                )
            # Sample data
            months = [str((i + 1) % 12 - 1) + "月" for i in range(4, 4 + 12)]
            actual_sales = [
                1000,
                1200,
                900,
                1100,
                950,
                1300,
                1400,
                1150,
                1000,
                1050,
                1200,
                1300,
            ]
            target_sales = [
                1100,
                1300,
                950,
                1200,
                1000,
                1400,
                1500,
                1250,
                1100,
                1150,
                1300,
                1400,
            ]

            # Create bar plot
            fig = go.Figure(
                data=[
                    go.Bar(name="Actual Sales", x=months, y=actual_sales),
                    go.Bar(name="Target Sales", x=months, y=target_sales),
                ]
            )

            # Update layout
            fig.update_layout(
                height=200,
                yaxis_title="Sales",
                barmode="group",
                margin=dict(t=0, b=0, l=0, r=0),
            )

            # Plot!
            st.plotly_chart(fig, use_container_width=True)

    with col2:
        with st.expander("システム稼働状況", expanded=True):
            st.table(pd.DataFrame(np.random.randn(10, 5)))


def get_monthly():
    col1, col2, col3, col4, _, _ = st.columns(6)
    with col2:
        year = st.selectbox(
            label="",
            options=["2023", "2024"],
        )
    with col3:
        month = st.selectbox(
            "月",
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
        )
    with col1:
        st.button("←")
    with col4:
        st.button("→")


def get_today():
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("グラフ", expanded=True):
            today = datetime.now(timezone(timedelta(hours=9)))
            x = pd.date_range(today, periods=48, freq="0.5H")

            fig = go.Figure(
                data=[
                    go.Scatter(
                        x=x,
                        y=np.random.randn(48),
                        mode="lines",
                        line=dict(color="#ff7f0e", width=2, shape="hv"),
                    ),
                ]
            )

        # Update layout
        fig.update_layout(
            height=200,
            yaxis_title="Sales",
            barmode="group",
            margin=dict(t=0, b=0, l=0, r=0),
        )
        st.plotly_chart(fig, use_container_width=True)


if menu == "dashboard":
    tabs = st.tabs(["Summary", "Monthly Report", "History"])
    with tabs[0]:
        get_summary()
    with tabs[1]:
        get_monthly()
    with tabs[2]:
        get_today()
