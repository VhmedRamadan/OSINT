from pyvis.network import Network
from scraper.scraper import get_followers


def build_graph(username, limit=10, max_depth=2):

    net = Network(height="600px", width="100%", directed=True)
    visited = set()

    # -----------------------------
    # RECURSIVE FUNCTION
    # -----------------------------
    def add_user(user, level=0):

        # stop conditions
        if user in visited:
            return

        if level > max_depth:
            return

        visited.add(user)

        # -----------------------------
        # NODE STYLE + METADATA
        # -----------------------------
        if level == 0:
            net.add_node(
                user,
                label=user,
                color="red",
                title=f"Target User: {user}"
            )
        else:
            net.add_node(
                user,
                label=user,
                color="lightblue",
                title=f"Level {level} connection"
            )

        # -----------------------------
        # GET FOLLOWERS
        # -----------------------------
        followers = get_followers(user, limit) or []

        if not followers:
            return

        for f in followers:

            # add follower node
            net.add_node(
                f,
                label=f,
                color="orange",
                title=f"Follower of {user}"
            )

            # -----------------------------
            # ADD EDGE WITH RELATION
            # -----------------------------
            net.add_edge(
                user,
                f,
                title="follows",
                label="follows"
            )

            # recursive call
            add_user(f, level + 1)

    # -----------------------------
    # START GRAPH
    # -----------------------------
    add_user(username)

    # -----------------------------
    # GRAPH SETTINGS (IMPORTANT 🔥)
    # -----------------------------
    net.set_options("""
    var options = {
      "nodes": {
        "shape": "dot",
        "size": 15,
        "font": { "size": 14 }
      },
      "edges": {
        "arrows": { "to": { "enabled": true } }
      },
      "physics": {
        "enabled": true
      }
    }
    """)

    # -----------------------------
    # SAVE FILE
    # -----------------------------
    file_name = f"{username}_graph.html"
    net.write_html(file_name)

    return file_name
