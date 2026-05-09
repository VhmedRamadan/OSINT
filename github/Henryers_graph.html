<html>
    <head>
        <meta charset="utf-8">
        
            <script src="lib/bindings/utils.js"></script>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.2/dist/dist/vis-network.min.css" integrity="sha512-WgxfT5LWjfszlPHXRmBWHkV2eceiWTOBvrKCNbdgDYTHrT2AeLCGbF4sZlZw3UMN3WtL0tGUoIAKsu8mllg/XA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
            <script src="https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.2/dist/vis-network.min.js" integrity="sha512-LnvoEWDFrqGHlHmDD2101OrLcbsfkrzoSpvtSQtxK3RMnRV0eOkhhBN2dXHKRrUU8p2DGRTk35n4O8nWSVe1mQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
            
        
<center>
<h1></h1>
</center>

<!-- <link rel="stylesheet" href="../node_modules/vis/dist/vis.min.css" type="text/css" />
<script type="text/javascript" src="../node_modules/vis/dist/vis.js"> </script>-->
        <link
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"
          rel="stylesheet"
          integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6"
          crossorigin="anonymous"
        />
        <script
          src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js"
          integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf"
          crossorigin="anonymous"
        ></script>


        <center>
          <h1></h1>
        </center>
        <style type="text/css">

             #mynetwork {
                 width: 100%;
                 height: 600px;
                 background-color: #ffffff;
                 border: 1px solid lightgray;
                 position: relative;
                 float: left;
             }

             
             #loadingBar {
                 position:absolute;
                 top:0px;
                 left:0px;
                 width: 100%;
                 height: 600px;
                 background-color:rgba(200,200,200,0.8);
                 -webkit-transition: all 0.5s ease;
                 -moz-transition: all 0.5s ease;
                 -ms-transition: all 0.5s ease;
                 -o-transition: all 0.5s ease;
                 transition: all 0.5s ease;
                 opacity:1;
             }

             #bar {
                 position:absolute;
                 top:0px;
                 left:0px;
                 width:20px;
                 height:20px;
                 margin:auto auto auto auto;
                 border-radius:11px;
                 border:2px solid rgba(30,30,30,0.05);
                 background: rgb(0, 173, 246); /* Old browsers */
                 box-shadow: 2px 0px 4px rgba(0,0,0,0.4);
             }

             #border {
                 position:absolute;
                 top:10px;
                 left:10px;
                 width:500px;
                 height:23px;
                 margin:auto auto auto auto;
                 box-shadow: 0px 0px 4px rgba(0,0,0,0.2);
                 border-radius:10px;
             }

             #text {
                 position:absolute;
                 top:8px;
                 left:530px;
                 width:30px;
                 height:50px;
                 margin:auto auto auto auto;
                 font-size:22px;
                 color: #000000;
             }

             div.outerBorder {
                 position:relative;
                 top:400px;
                 width:600px;
                 height:44px;
                 margin:auto auto auto auto;
                 border:8px solid rgba(0,0,0,0.1);
                 background: rgb(252,252,252); /* Old browsers */
                 background: -moz-linear-gradient(top,  rgba(252,252,252,1) 0%, rgba(237,237,237,1) 100%); /* FF3.6+ */
                 background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,rgba(252,252,252,1)), color-stop(100%,rgba(237,237,237,1))); /* Chrome,Safari4+ */
                 background: -webkit-linear-gradient(top,  rgba(252,252,252,1) 0%,rgba(237,237,237,1) 100%); /* Chrome10+,Safari5.1+ */
                 background: -o-linear-gradient(top,  rgba(252,252,252,1) 0%,rgba(237,237,237,1) 100%); /* Opera 11.10+ */
                 background: -ms-linear-gradient(top,  rgba(252,252,252,1) 0%,rgba(237,237,237,1) 100%); /* IE10+ */
                 background: linear-gradient(to bottom,  rgba(252,252,252,1) 0%,rgba(237,237,237,1) 100%); /* W3C */
                 filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#fcfcfc', endColorstr='#ededed',GradientType=0 ); /* IE6-9 */
                 border-radius:72px;
                 box-shadow: 0px 0px 10px rgba(0,0,0,0.2);
             }
             

             

             
        </style>
    </head>


    <body>
        <div class="card" style="width: 100%">
            
            
            <div id="mynetwork" class="card-body"></div>
        </div>

        
            <div id="loadingBar">
              <div class="outerBorder">
                <div id="text">0%</div>
                <div id="border">
                  <div id="bar"></div>
                </div>
              </div>
            </div>
        
        

        <script type="text/javascript">

              // initialize global variables.
              var edges;
              var nodes;
              var allNodes;
              var allEdges;
              var nodeColors;
              var originalNodes;
              var network;
              var container;
              var options, data;
              var filter = {
                  item : '',
                  property : '',
                  value : []
              };

              

              

              // This method is responsible for drawing the graph, returns the drawn network
              function drawGraph() {
                  var container = document.getElementById('mynetwork');

                  

                  // parsing and collecting nodes and edges from the python
                  nodes = new vis.DataSet([{"color": "red", "id": "Henryers", "label": "Henryers", "shape": "dot", "title": "Target User: Henryers"}, {"color": "orange", "id": "hawskpy", "label": "hawskpy", "shape": "dot", "title": "Follower of Henryers"}, {"color": "orange", "id": "esin", "label": "esin", "shape": "dot", "title": "Follower of hawskpy"}, {"color": "orange", "id": "jacques", "label": "jacques", "shape": "dot", "title": "Follower of esin"}, {"color": "orange", "id": "wilburhimself", "label": "wilburhimself", "shape": "dot", "title": "Follower of esin"}, {"color": "orange", "id": "copyleftdev", "label": "copyleftdev", "shape": "dot", "title": "Follower of esin"}, {"color": "orange", "id": "matiasinsaurralde", "label": "matiasinsaurralde", "shape": "dot", "title": "Follower of esin"}, {"color": "orange", "id": "4eek", "label": "4eek", "shape": "dot", "title": "Follower of esin"}, {"color": "orange", "id": "rohithadassanayake", "label": "rohithadassanayake", "shape": "dot", "title": "Follower of hawskpy"}, {"color": "orange", "id": "okiess", "label": "okiess", "shape": "dot", "title": "Follower of rohithadassanayake"}, {"color": "orange", "id": "alibby", "label": "alibby", "shape": "dot", "title": "Follower of rohithadassanayake"}, {"color": "orange", "id": "spnkr", "label": "spnkr", "shape": "dot", "title": "Follower of rohithadassanayake"}, {"color": "orange", "id": "STRd6", "label": "STRd6", "shape": "dot", "title": "Follower of rohithadassanayake"}, {"color": "orange", "id": "niiamon", "label": "niiamon", "shape": "dot", "title": "Follower of rohithadassanayake"}, {"color": "orange", "id": "umairsalam", "label": "umairsalam", "shape": "dot", "title": "Follower of hawskpy"}, {"color": "orange", "id": "KevinHock", "label": "KevinHock", "shape": "dot", "title": "Follower of umairsalam"}, {"color": "orange", "id": "idimetrix", "label": "idimetrix", "shape": "dot", "title": "Follower of umairsalam"}, {"color": "orange", "id": "mustafacagri", "label": "mustafacagri", "shape": "dot", "title": "Follower of umairsalam"}, {"color": "orange", "id": "Connor9994", "label": "Connor9994", "shape": "dot", "title": "Follower of umairsalam"}, {"color": "orange", "id": "OfficialCodeVoyage", "label": "OfficialCodeVoyage", "shape": "dot", "title": "Follower of umairsalam"}, {"color": "orange", "id": "lipi042222", "label": "lipi042222", "shape": "dot", "title": "Follower of hawskpy"}, {"color": "orange", "id": "mattn", "label": "mattn", "shape": "dot", "title": "Follower of lipi042222"}, {"color": "orange", "id": "frankel", "label": "frankel", "shape": "dot", "title": "Follower of lipi042222"}, {"color": "orange", "id": "pascalgn", "label": "pascalgn", "shape": "dot", "title": "Follower of lipi042222"}, {"color": "orange", "id": "manageyp", "label": "manageyp", "shape": "dot", "title": "Follower of lipi042222"}, {"color": "orange", "id": "lxp135", "label": "lxp135", "shape": "dot", "title": "Follower of hawskpy"}, {"color": "orange", "id": "mikegwhit", "label": "mikegwhit", "shape": "dot", "title": "Follower of lxp135"}, {"color": "orange", "id": "neodigm", "label": "neodigm", "shape": "dot", "title": "Follower of lxp135"}, {"color": "orange", "id": "cusspvz", "label": "cusspvz", "shape": "dot", "title": "Follower of lxp135"}, {"color": "orange", "id": "dannyrb", "label": "dannyrb", "shape": "dot", "title": "Follower of lxp135"}, {"color": "orange", "id": "gamemann", "label": "gamemann", "shape": "dot", "title": "Follower of Henryers"}, {"color": "orange", "id": "bumi", "label": "bumi", "shape": "dot", "title": "Follower of okiess"}, {"color": "orange", "id": "intabulas", "label": "intabulas", "shape": "dot", "title": "Follower of okiess"}, {"color": "orange", "id": "peterlih", "label": "peterlih", "shape": "dot", "title": "Follower of okiess"}, {"color": "orange", "id": "ethem", "label": "ethem", "shape": "dot", "title": "Follower of okiess"}, {"color": "orange", "id": "henrysher", "label": "henrysher", "shape": "dot", "title": "Follower of okiess"}, {"color": "orange", "id": "jthomp", "label": "jthomp", "shape": "dot", "title": "Follower of gamemann"}, {"color": "orange", "id": "peterruler", "label": "peterruler", "shape": "dot", "title": "Follower of jthomp"}, {"color": "orange", "id": "ahmetabdi", "label": "ahmetabdi", "shape": "dot", "title": "Follower of jthomp"}, {"color": "orange", "id": "0xVortex", "label": "0xVortex", "shape": "dot", "title": "Follower of jthomp"}, {"color": "orange", "id": "angusshire", "label": "angusshire", "shape": "dot", "title": "Follower of jthomp"}, {"color": "orange", "id": "anderson", "label": "anderson", "shape": "dot", "title": "Follower of gamemann"}, {"color": "orange", "id": "digdog", "label": "digdog", "shape": "dot", "title": "Follower of anderson"}, {"color": "orange", "id": "eaquiroz", "label": "eaquiroz", "shape": "dot", "title": "Follower of anderson"}, {"color": "orange", "id": "batermj", "label": "batermj", "shape": "dot", "title": "Follower of anderson"}, {"color": "orange", "id": "WillemJan", "label": "WillemJan", "shape": "dot", "title": "Follower of anderson"}, {"color": "orange", "id": "laquereric", "label": "laquereric", "shape": "dot", "title": "Follower of gamemann"}, {"color": "orange", "id": "kairichard", "label": "kairichard", "shape": "dot", "title": "Follower of laquereric"}, {"color": "orange", "id": "bcavileer", "label": "bcavileer", "shape": "dot", "title": "Follower of laquereric"}, {"color": "orange", "id": "ableasdale", "label": "ableasdale", "shape": "dot", "title": "Follower of laquereric"}, {"color": "orange", "id": "grantbdev", "label": "grantbdev", "shape": "dot", "title": "Follower of laquereric"}, {"color": "orange", "id": "bennyzen", "label": "bennyzen", "shape": "dot", "title": "Follower of gamemann"}, {"color": "orange", "id": "stickgrinder", "label": "stickgrinder", "shape": "dot", "title": "Follower of bennyzen"}, {"color": "orange", "id": "trinhminhtriet", "label": "trinhminhtriet", "shape": "dot", "title": "Follower of bennyzen"}, {"color": "orange", "id": "amadeusp", "label": "amadeusp", "shape": "dot", "title": "Follower of bennyzen"}, {"color": "orange", "id": "KylerCondran", "label": "KylerCondran", "shape": "dot", "title": "Follower of Henryers"}, {"color": "orange", "id": "linces", "label": "linces", "shape": "dot", "title": "Follower of KylerCondran"}, {"color": "orange", "id": "Theosis", "label": "Theosis", "shape": "dot", "title": "Follower of linces"}, {"color": "orange", "id": "dmitrysobolev", "label": "dmitrysobolev", "shape": "dot", "title": "Follower of linces"}, {"color": "orange", "id": "Boyquotes", "label": "Boyquotes", "shape": "dot", "title": "Follower of linces"}, {"color": "orange", "id": "maniamadrid", "label": "maniamadrid", "shape": "dot", "title": "Follower of KylerCondran"}, {"color": "orange", "id": "kenjinote", "label": "kenjinote", "shape": "dot", "title": "Follower of maniamadrid"}, {"color": "orange", "id": "tech4xstar", "label": "tech4xstar", "shape": "dot", "title": "Follower of maniamadrid"}, {"color": "orange", "id": "ndolocr", "label": "ndolocr", "shape": "dot", "title": "Follower of maniamadrid"}, {"color": "orange", "id": "yoosofan", "label": "yoosofan", "shape": "dot", "title": "Follower of KylerCondran"}, {"color": "orange", "id": "codebrainz", "label": "codebrainz", "shape": "dot", "title": "Follower of yoosofan"}, {"color": "orange", "id": "levonk", "label": "levonk", "shape": "dot", "title": "Follower of yoosofan"}, {"color": "orange", "id": "slavaGanzin", "label": "slavaGanzin", "shape": "dot", "title": "Follower of yoosofan"}, {"color": "orange", "id": "palonza", "label": "palonza", "shape": "dot", "title": "Follower of KylerCondran"}, {"color": "orange", "id": "dimitre", "label": "dimitre", "shape": "dot", "title": "Follower of palonza"}, {"color": "orange", "id": "mrothauer", "label": "mrothauer", "shape": "dot", "title": "Follower of palonza"}, {"color": "orange", "id": "marialobillo", "label": "marialobillo", "shape": "dot", "title": "Follower of palonza"}, {"color": "orange", "id": "andytriboletti", "label": "andytriboletti", "shape": "dot", "title": "Follower of levonk"}, {"color": "orange", "id": "kabaka", "label": "kabaka", "shape": "dot", "title": "Follower of levonk"}, {"color": "orange", "id": "wenceslau", "label": "wenceslau", "shape": "dot", "title": "Follower of levonk"}, {"color": "orange", "id": "johndpope", "label": "johndpope", "shape": "dot", "title": "Follower of levonk"}, {"color": "orange", "id": "yq60523", "label": "yq60523", "shape": "dot", "title": "Follower of Henryers"}, {"color": "orange", "id": "Arcko", "label": "Arcko", "shape": "dot", "title": "Follower of idimetrix"}, {"color": "orange", "id": "eduardoj", "label": "eduardoj", "shape": "dot", "title": "Follower of idimetrix"}, {"color": "orange", "id": "ambreshbiradar9", "label": "ambreshbiradar9", "shape": "dot", "title": "Follower of yq60523"}, {"color": "orange", "id": "RickeyEstes", "label": "RickeyEstes", "shape": "dot", "title": "Follower of ambreshbiradar9"}, {"color": "orange", "id": "IDouble", "label": "IDouble", "shape": "dot", "title": "Follower of ambreshbiradar9"}, {"color": "orange", "id": "standardgalactic", "label": "standardgalactic", "shape": "dot", "title": "Follower of ambreshbiradar9"}, {"color": "orange", "id": "brahmadathanvb", "label": "brahmadathanvb", "shape": "dot", "title": "Follower of ambreshbiradar9"}, {"color": "orange", "id": "jjdunlop", "label": "jjdunlop", "shape": "dot", "title": "Follower of ambreshbiradar9"}, {"color": "orange", "id": "Vesuvius6", "label": "Vesuvius6", "shape": "dot", "title": "Follower of yq60523"}, {"color": "orange", "id": "lrlgogo", "label": "lrlgogo", "shape": "dot", "title": "Follower of yq60523"}, {"color": "orange", "id": "LeonShe", "label": "LeonShe", "shape": "dot", "title": "Follower of lrlgogo"}, {"color": "orange", "id": "chenfang0616", "label": "chenfang0616", "shape": "dot", "title": "Follower of lrlgogo"}, {"color": "orange", "id": "1997030303", "label": "1997030303", "shape": "dot", "title": "Follower of lrlgogo"}, {"color": "orange", "id": "mahak92", "label": "mahak92", "shape": "dot", "title": "Follower of lrlgogo"}, {"color": "orange", "id": "wangpo1991", "label": "wangpo1991", "shape": "dot", "title": "Follower of yq60523"}, {"color": "orange", "id": "wb02125055", "label": "wb02125055", "shape": "dot", "title": "Follower of wangpo1991"}, {"color": "orange", "id": "kulikov-dev", "label": "kulikov-dev", "shape": "dot", "title": "Follower of wangpo1991"}, {"color": "orange", "id": "ahsewm", "label": "ahsewm", "shape": "dot", "title": "Follower of wangpo1991"}, {"color": "orange", "id": "jelspace", "label": "jelspace", "shape": "dot", "title": "Follower of Henryers"}, {"color": "orange", "id": "kevindamm", "label": "kevindamm", "shape": "dot", "title": "Follower of jelspace"}, {"color": "orange", "id": "riseansmal", "label": "riseansmal", "shape": "dot", "title": "Follower of kevindamm"}, {"color": "orange", "id": "WildGenie", "label": "WildGenie", "shape": "dot", "title": "Follower of jelspace"}, {"color": "orange", "id": "CetinSert", "label": "CetinSert", "shape": "dot", "title": "Follower of WildGenie"}, {"color": "orange", "id": "mennan", "label": "mennan", "shape": "dot", "title": "Follower of WildGenie"}, {"color": "orange", "id": "galaris", "label": "galaris", "shape": "dot", "title": "Follower of WildGenie"}, {"color": "orange", "id": "trcjr", "label": "trcjr", "shape": "dot", "title": "Follower of jelspace"}, {"color": "orange", "id": "gugod", "label": "gugod", "shape": "dot", "title": "Follower of trcjr"}, {"color": "orange", "id": "zdk", "label": "zdk", "shape": "dot", "title": "Follower of trcjr"}, {"color": "orange", "id": "c9s", "label": "c9s", "shape": "dot", "title": "Follower of trcjr"}, {"color": "orange", "id": "tempire", "label": "tempire", "shape": "dot", "title": "Follower of trcjr"}]);
                  edges = new vis.DataSet([{"arrows": "to", "from": "Henryers", "label": "follows", "title": "follows", "to": "hawskpy"}, {"arrows": "to", "from": "hawskpy", "label": "follows", "title": "follows", "to": "esin"}, {"arrows": "to", "from": "esin", "label": "follows", "title": "follows", "to": "jacques"}, {"arrows": "to", "from": "esin", "label": "follows", "title": "follows", "to": "wilburhimself"}, {"arrows": "to", "from": "esin", "label": "follows", "title": "follows", "to": "copyleftdev"}, {"arrows": "to", "from": "esin", "label": "follows", "title": "follows", "to": "matiasinsaurralde"}, {"arrows": "to", "from": "esin", "label": "follows", "title": "follows", "to": "4eek"}, {"arrows": "to", "from": "hawskpy", "label": "follows", "title": "follows", "to": "rohithadassanayake"}, {"arrows": "to", "from": "rohithadassanayake", "label": "follows", "title": "follows", "to": "okiess"}, {"arrows": "to", "from": "rohithadassanayake", "label": "follows", "title": "follows", "to": "alibby"}, {"arrows": "to", "from": "rohithadassanayake", "label": "follows", "title": "follows", "to": "spnkr"}, {"arrows": "to", "from": "rohithadassanayake", "label": "follows", "title": "follows", "to": "STRd6"}, {"arrows": "to", "from": "rohithadassanayake", "label": "follows", "title": "follows", "to": "niiamon"}, {"arrows": "to", "from": "hawskpy", "label": "follows", "title": "follows", "to": "umairsalam"}, {"arrows": "to", "from": "umairsalam", "label": "follows", "title": "follows", "to": "KevinHock"}, {"arrows": "to", "from": "umairsalam", "label": "follows", "title": "follows", "to": "idimetrix"}, {"arrows": "to", "from": "umairsalam", "label": "follows", "title": "follows", "to": "mustafacagri"}, {"arrows": "to", "from": "umairsalam", "label": "follows", "title": "follows", "to": "Connor9994"}, {"arrows": "to", "from": "umairsalam", "label": "follows", "title": "follows", "to": "OfficialCodeVoyage"}, {"arrows": "to", "from": "hawskpy", "label": "follows", "title": "follows", "to": "lipi042222"}, {"arrows": "to", "from": "lipi042222", "label": "follows", "title": "follows", "to": "mattn"}, {"arrows": "to", "from": "lipi042222", "label": "follows", "title": "follows", "to": "frankel"}, {"arrows": "to", "from": "lipi042222", "label": "follows", "title": "follows", "to": "esin"}, {"arrows": "to", "from": "lipi042222", "label": "follows", "title": "follows", "to": "pascalgn"}, {"arrows": "to", "from": "lipi042222", "label": "follows", "title": "follows", "to": "manageyp"}, {"arrows": "to", "from": "hawskpy", "label": "follows", "title": "follows", "to": "lxp135"}, {"arrows": "to", "from": "lxp135", "label": "follows", "title": "follows", "to": "mikegwhit"}, {"arrows": "to", "from": "lxp135", "label": "follows", "title": "follows", "to": "neodigm"}, {"arrows": "to", "from": "lxp135", "label": "follows", "title": "follows", "to": "hawskpy"}, {"arrows": "to", "from": "lxp135", "label": "follows", "title": "follows", "to": "cusspvz"}, {"arrows": "to", "from": "lxp135", "label": "follows", "title": "follows", "to": "dannyrb"}, {"arrows": "to", "from": "Henryers", "label": "follows", "title": "follows", "to": "gamemann"}, {"arrows": "to", "from": "gamemann", "label": "follows", "title": "follows", "to": "okiess"}, {"arrows": "to", "from": "okiess", "label": "follows", "title": "follows", "to": "bumi"}, {"arrows": "to", "from": "okiess", "label": "follows", "title": "follows", "to": "intabulas"}, {"arrows": "to", "from": "okiess", "label": "follows", "title": "follows", "to": "peterlih"}, {"arrows": "to", "from": "okiess", "label": "follows", "title": "follows", "to": "ethem"}, {"arrows": "to", "from": "okiess", "label": "follows", "title": "follows", "to": "henrysher"}, {"arrows": "to", "from": "gamemann", "label": "follows", "title": "follows", "to": "jthomp"}, {"arrows": "to", "from": "jthomp", "label": "follows", "title": "follows", "to": "peterruler"}, {"arrows": "to", "from": "jthomp", "label": "follows", "title": "follows", "to": "ahmetabdi"}, {"arrows": "to", "from": "jthomp", "label": "follows", "title": "follows", "to": "KevinHock"}, {"arrows": "to", "from": "jthomp", "label": "follows", "title": "follows", "to": "0xVortex"}, {"arrows": "to", "from": "jthomp", "label": "follows", "title": "follows", "to": "angusshire"}, {"arrows": "to", "from": "gamemann", "label": "follows", "title": "follows", "to": "anderson"}, {"arrows": "to", "from": "anderson", "label": "follows", "title": "follows", "to": "STRd6"}, {"arrows": "to", "from": "anderson", "label": "follows", "title": "follows", "to": "digdog"}, {"arrows": "to", "from": "anderson", "label": "follows", "title": "follows", "to": "eaquiroz"}, {"arrows": "to", "from": "anderson", "label": "follows", "title": "follows", "to": "batermj"}, {"arrows": "to", "from": "anderson", "label": "follows", "title": "follows", "to": "WillemJan"}, {"arrows": "to", "from": "gamemann", "label": "follows", "title": "follows", "to": "laquereric"}, {"arrows": "to", "from": "laquereric", "label": "follows", "title": "follows", "to": "kairichard"}, {"arrows": "to", "from": "laquereric", "label": "follows", "title": "follows", "to": "bcavileer"}, {"arrows": "to", "from": "laquereric", "label": "follows", "title": "follows", "to": "ableasdale"}, {"arrows": "to", "from": "laquereric", "label": "follows", "title": "follows", "to": "peterruler"}, {"arrows": "to", "from": "laquereric", "label": "follows", "title": "follows", "to": "grantbdev"}, {"arrows": "to", "from": "gamemann", "label": "follows", "title": "follows", "to": "bennyzen"}, {"arrows": "to", "from": "bennyzen", "label": "follows", "title": "follows", "to": "stickgrinder"}, {"arrows": "to", "from": "bennyzen", "label": "follows", "title": "follows", "to": "trinhminhtriet"}, {"arrows": "to", "from": "bennyzen", "label": "follows", "title": "follows", "to": "amadeusp"}, {"arrows": "to", "from": "bennyzen", "label": "follows", "title": "follows", "to": "KevinHock"}, {"arrows": "to", "from": "bennyzen", "label": "follows", "title": "follows", "to": "angusshire"}, {"arrows": "to", "from": "Henryers", "label": "follows", "title": "follows", "to": "KylerCondran"}, {"arrows": "to", "from": "KylerCondran", "label": "follows", "title": "follows", "to": "linces"}, {"arrows": "to", "from": "linces", "label": "follows", "title": "follows", "to": "Theosis"}, {"arrows": "to", "from": "linces", "label": "follows", "title": "follows", "to": "esin"}, {"arrows": "to", "from": "linces", "label": "follows", "title": "follows", "to": "dmitrysobolev"}, {"arrows": "to", "from": "linces", "label": "follows", "title": "follows", "to": "batermj"}, {"arrows": "to", "from": "linces", "label": "follows", "title": "follows", "to": "Boyquotes"}, {"arrows": "to", "from": "KylerCondran", "label": "follows", "title": "follows", "to": "maniamadrid"}, {"arrows": "to", "from": "maniamadrid", "label": "follows", "title": "follows", "to": "peterruler"}, {"arrows": "to", "from": "maniamadrid", "label": "follows", "title": "follows", "to": "kenjinote"}, {"arrows": "to", "from": "maniamadrid", "label": "follows", "title": "follows", "to": "KevinHock"}, {"arrows": "to", "from": "maniamadrid", "label": "follows", "title": "follows", "to": "tech4xstar"}, {"arrows": "to", "from": "maniamadrid", "label": "follows", "title": "follows", "to": "ndolocr"}, {"arrows": "to", "from": "KylerCondran", "label": "follows", "title": "follows", "to": "yoosofan"}, {"arrows": "to", "from": "yoosofan", "label": "follows", "title": "follows", "to": "esin"}, {"arrows": "to", "from": "yoosofan", "label": "follows", "title": "follows", "to": "codebrainz"}, {"arrows": "to", "from": "yoosofan", "label": "follows", "title": "follows", "to": "levonk"}, {"arrows": "to", "from": "yoosofan", "label": "follows", "title": "follows", "to": "peterruler"}, {"arrows": "to", "from": "yoosofan", "label": "follows", "title": "follows", "to": "slavaGanzin"}, {"arrows": "to", "from": "KylerCondran", "label": "follows", "title": "follows", "to": "palonza"}, {"arrows": "to", "from": "palonza", "label": "follows", "title": "follows", "to": "dimitre"}, {"arrows": "to", "from": "palonza", "label": "follows", "title": "follows", "to": "mrothauer"}, {"arrows": "to", "from": "palonza", "label": "follows", "title": "follows", "to": "peterruler"}, {"arrows": "to", "from": "palonza", "label": "follows", "title": "follows", "to": "slavaGanzin"}, {"arrows": "to", "from": "palonza", "label": "follows", "title": "follows", "to": "marialobillo"}, {"arrows": "to", "from": "KylerCondran", "label": "follows", "title": "follows", "to": "levonk"}, {"arrows": "to", "from": "levonk", "label": "follows", "title": "follows", "to": "andytriboletti"}, {"arrows": "to", "from": "levonk", "label": "follows", "title": "follows", "to": "yoosofan"}, {"arrows": "to", "from": "levonk", "label": "follows", "title": "follows", "to": "kabaka"}, {"arrows": "to", "from": "levonk", "label": "follows", "title": "follows", "to": "wenceslau"}, {"arrows": "to", "from": "levonk", "label": "follows", "title": "follows", "to": "johndpope"}, {"arrows": "to", "from": "Henryers", "label": "follows", "title": "follows", "to": "yq60523"}, {"arrows": "to", "from": "yq60523", "label": "follows", "title": "follows", "to": "idimetrix"}, {"arrows": "to", "from": "idimetrix", "label": "follows", "title": "follows", "to": "okiess"}, {"arrows": "to", "from": "idimetrix", "label": "follows", "title": "follows", "to": "jthomp"}, {"arrows": "to", "from": "idimetrix", "label": "follows", "title": "follows", "to": "wilburhimself"}, {"arrows": "to", "from": "idimetrix", "label": "follows", "title": "follows", "to": "Arcko"}, {"arrows": "to", "from": "idimetrix", "label": "follows", "title": "follows", "to": "eduardoj"}, {"arrows": "to", "from": "yq60523", "label": "follows", "title": "follows", "to": "ambreshbiradar9"}, {"arrows": "to", "from": "ambreshbiradar9", "label": "follows", "title": "follows", "to": "RickeyEstes"}, {"arrows": "to", "from": "ambreshbiradar9", "label": "follows", "title": "follows", "to": "IDouble"}, {"arrows": "to", "from": "ambreshbiradar9", "label": "follows", "title": "follows", "to": "standardgalactic"}, {"arrows": "to", "from": "ambreshbiradar9", "label": "follows", "title": "follows", "to": "brahmadathanvb"}, {"arrows": "to", "from": "ambreshbiradar9", "label": "follows", "title": "follows", "to": "jjdunlop"}, {"arrows": "to", "from": "yq60523", "label": "follows", "title": "follows", "to": "Vesuvius6"}, {"arrows": "to", "from": "yq60523", "label": "follows", "title": "follows", "to": "lrlgogo"}, {"arrows": "to", "from": "lrlgogo", "label": "follows", "title": "follows", "to": "yq60523"}, {"arrows": "to", "from": "lrlgogo", "label": "follows", "title": "follows", "to": "LeonShe"}, {"arrows": "to", "from": "lrlgogo", "label": "follows", "title": "follows", "to": "chenfang0616"}, {"arrows": "to", "from": "lrlgogo", "label": "follows", "title": "follows", "to": "1997030303"}, {"arrows": "to", "from": "lrlgogo", "label": "follows", "title": "follows", "to": "mahak92"}, {"arrows": "to", "from": "yq60523", "label": "follows", "title": "follows", "to": "wangpo1991"}, {"arrows": "to", "from": "wangpo1991", "label": "follows", "title": "follows", "to": "wb02125055"}, {"arrows": "to", "from": "wangpo1991", "label": "follows", "title": "follows", "to": "kulikov-dev"}, {"arrows": "to", "from": "wangpo1991", "label": "follows", "title": "follows", "to": "ahsewm"}, {"arrows": "to", "from": "Henryers", "label": "follows", "title": "follows", "to": "jelspace"}, {"arrows": "to", "from": "jelspace", "label": "follows", "title": "follows", "to": "kevindamm"}, {"arrows": "to", "from": "kevindamm", "label": "follows", "title": "follows", "to": "peterruler"}, {"arrows": "to", "from": "kevindamm", "label": "follows", "title": "follows", "to": "ndolocr"}, {"arrows": "to", "from": "kevindamm", "label": "follows", "title": "follows", "to": "angusshire"}, {"arrows": "to", "from": "kevindamm", "label": "follows", "title": "follows", "to": "riseansmal"}, {"arrows": "to", "from": "kevindamm", "label": "follows", "title": "follows", "to": "mustafacagri"}, {"arrows": "to", "from": "jelspace", "label": "follows", "title": "follows", "to": "WildGenie"}, {"arrows": "to", "from": "WildGenie", "label": "follows", "title": "follows", "to": "CetinSert"}, {"arrows": "to", "from": "WildGenie", "label": "follows", "title": "follows", "to": "esin"}, {"arrows": "to", "from": "WildGenie", "label": "follows", "title": "follows", "to": "mennan"}, {"arrows": "to", "from": "WildGenie", "label": "follows", "title": "follows", "to": "batermj"}, {"arrows": "to", "from": "WildGenie", "label": "follows", "title": "follows", "to": "galaris"}, {"arrows": "to", "from": "jelspace", "label": "follows", "title": "follows", "to": "trcjr"}, {"arrows": "to", "from": "trcjr", "label": "follows", "title": "follows", "to": "gugod"}, {"arrows": "to", "from": "trcjr", "label": "follows", "title": "follows", "to": "zdk"}, {"arrows": "to", "from": "trcjr", "label": "follows", "title": "follows", "to": "c9s"}, {"arrows": "to", "from": "trcjr", "label": "follows", "title": "follows", "to": "tempire"}, {"arrows": "to", "from": "trcjr", "label": "follows", "title": "follows", "to": "levonk"}, {"arrows": "to", "from": "jelspace", "label": "follows", "title": "follows", "to": "esin"}, {"arrows": "to", "from": "jelspace", "label": "follows", "title": "follows", "to": "maniamadrid"}]);

                  nodeColors = {};
                  allNodes = nodes.get({ returnType: "Object" });
                  for (nodeId in allNodes) {
                    nodeColors[nodeId] = allNodes[nodeId].color;
                  }
                  allEdges = edges.get({ returnType: "Object" });
                  // adding nodes and edges to the graph
                  data = {nodes: nodes, edges: edges};

                  var options = {"nodes": {"shape": "dot", "size": 15, "font": {"size": 14}}, "edges": {"arrows": {"to": {"enabled": true}}}, "physics": {"enabled": true}};

                  


                  

                  network = new vis.Network(container, data, options);

                  

                  

                  


                  
                      network.on("stabilizationProgress", function(params) {
                          document.getElementById('loadingBar').removeAttribute("style");
                          var maxWidth = 496;
                          var minWidth = 20;
                          var widthFactor = params.iterations/params.total;
                          var width = Math.max(minWidth,maxWidth * widthFactor);
                          document.getElementById('bar').style.width = width + 'px';
                          document.getElementById('text').innerHTML = Math.round(widthFactor*100) + '%';
                      });
                      network.once("stabilizationIterationsDone", function() {
                          document.getElementById('text').innerHTML = '100%';
                          document.getElementById('bar').style.width = '496px';
                          document.getElementById('loadingBar').style.opacity = 0;
                          // really clean the dom element
                          setTimeout(function () {document.getElementById('loadingBar').style.display = 'none';}, 500);
                      });
                  

                  return network;

              }
              drawGraph();
        </script>
    </body>
</html>