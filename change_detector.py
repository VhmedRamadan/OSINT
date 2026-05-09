import streamlit as st
from scraper.scraper import get_github_user, save_snapshot
from graph.graph import build_graph
from change.change_detector import analyze_changes_ui
from osint_search import cross_platform_search
from deleted_recovery import detect_deleted_content
import streamlit.components.v1 as components


# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="OSINT GitHub Analyzer", layout="wide")

st.title("🧠 OSINT GitHub Analyzer")
st.write("Advanced Social Media Forensics Dashboard")


# -----------------------------
# INPUT
# -----------------------------
username = st.text_input("Enter GitHub username")


# -----------------------------
# RUN INVESTIGATION
# -----------------------------
if st.button("Run Investigation"):

    if not username:
        st.warning("Please enter a username")
        st.stop()

    # -----------------------------
    # LOADING STATE
    # -----------------------------
    with st.spinner("🧠 Running OSINT investigation..."):
        data = get_github_user(username)

    # -----------------------------
    # ERROR HANDLING
    # -----------------------------
    if isinstance(data, dict) and "error" in data:
        st.error(f"Error: {data['error']}")
        st.stop()

    if not data:
        st.error("User not found or API blocked")
        st.stop()

    st.success("User data collected successfully!")

    # -----------------------------
    # SAVE SNAPSHOT
    # -----------------------------
    save_snapshot(username, data)


    # -----------------------------
    # TABS
    # -----------------------------
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "👤 Profile",
        "🌐 Graph",
        "📊 Changes",
        "🔎 Cross-Platform",
        "🗑️ Deleted Recovery",
        "📑 Report"
    ])


    # -----------------------------
    # TAB 1 - PROFILE
    # -----------------------------
    with tab1:
        st.subheader("👤 Profile Information")

        col1, col2, col3 = st.columns(3)

        col1.metric("Followers", data.get("followers", 0))
        col2.metric("Following", data.get("following", 0))
        col3.metric("Repos", data.get("public_repos", 0))

        st.divider()

        st.json({
            "username": data.get("username"),
            "name": data.get("name"),
            "bio": data.get("bio"),
            "location": data.get("location"),
            "profile_url": data.get("profile_url"),
            "created_at": data.get("created_at"),
            "timestamp": data.get("timestamp")
        })


    # -----------------------------
    # TAB 2 - GRAPH
    # -----------------------------
    with tab2:
        st.subheader("🌐 Social Network Graph")

        graph_file = build_graph(username, limit=5)

        st.success("Graph generated successfully")

        with open(graph_file, "r", encoding="utf-8") as f:
            html = f.read()

        components.html(html, height=700, scrolling=True)


    # -----------------------------
    # TAB 3 - CHANGES
    # -----------------------------
    with tab3:
        st.subheader("📊 Snapshot Analysis")

        result = analyze_changes_ui(username)

        if result == "no_data":
            st.warning("No snapshots available")

        elif result == "only_one":
            st.info("Need at least 2 snapshots for comparison")

        elif not result or (result.get("status") == "success" and not result.get("data")):
            st.success("No changes detected")

        else:
            st.error("🚨 Changes Detected")

            changes = result.get("data", {})

            for key, value in changes.items():

                if key == "analysis_time":
                    continue

                st.markdown(f"### 🔹 {key}")

                st.write("Old:", value.get("old"))
                st.write("New:", value.get("new"))

                if "difference" in value:
                    st.write("Change:", value["difference"])

                if "alert" in value:
                    st.error(value["alert"])

                st.divider()


    # -----------------------------
    # TAB 4 - CROSS PLATFORM
    # -----------------------------
    with tab4:
        st.subheader("🔎 Cross-Platform OSINT Search")

        results = cross_platform_search(username)

        for platform, value in results.items():

            st.markdown(f"### 🔹 {platform}")

            if platform.lower() == "github":
                st.success(value)
            else:
                st.write(value)

        st.info("Simulated OSINT enumeration (educational purpose)")


    # -----------------------------
    # TAB 5 - DELETED CONTENT
    # -----------------------------
    with tab5:
        st.subheader("🗑️ Deleted Content Forensics")

        result = detect_deleted_content(username)

        if result == "not_enough_data":
            st.warning("Need at least 2 snapshots for analysis")

        elif not result:
            st.success("No deleted or modified content detected")

        else:
            st.error("🚨 Potential deleted/modified data detected")

            for key, value in result.items():

                st.markdown(f"### 🔹 {key}")
                st.write("Status:", value.get("status"))
                st.write("Old:", value.get("old"))
                st.write("New:", value.get("new"))

                if "severity" in value:
                    st.warning(f"Severity: {value['severity']}")

                st.divider()


    # -----------------------------
    # TAB 6 - FINAL REPORT
    # -----------------------------
    with tab6:
        st.subheader("📑 Investigation Report")

        st.json({
            "target": username,
            "profile": data,
            "changes": analyze_changes_ui(username),
            "graph_status": "generated",
            "timestamp": data.get("timestamp"),
            "status": "completed"
        })

        st.success("Report ready for export (future PDF feature)")
