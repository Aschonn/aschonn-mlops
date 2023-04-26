Command Help:

"dvc repro": Checks changes between current and previous models in pipeline.

tox command:
"tox"

tox rebuild:
"tox -r"

run through tests in pytest:
"pytest -v"

setup command:
"pip install -e ."

create build package, command:
"python setup.py sdist bdist_wheel"


<mxfile host="app.diagrams.net" modified="2023-04-26T17:37:52.135Z" agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36" etag="PGXt-9pkIZJ9We7GRIkp" version="21.2.2" type="github">
  <diagram name="Page-1" id="OHU9wAy245O7qlROUTTO">
    <mxGraphModel dx="1434" dy="796" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="dGWG_sC8McWYThyw6kNz-21" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="dGWG_sC8McWYThyw6kNz-1" target="dGWG_sC8McWYThyw6kNz-10">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="dGWG_sC8McWYThyw6kNz-22" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="dGWG_sC8McWYThyw6kNz-1" target="dGWG_sC8McWYThyw6kNz-16">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="dGWG_sC8McWYThyw6kNz-1" value="Website Creation" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="60" y="330" width="120" height="80" as="geometry" />
        </mxCell>
        <mxCell id="dGWG_sC8McWYThyw6kNz-42" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="dGWG_sC8McWYThyw6kNz-2" target="dGWG_sC8McWYThyw6kNz-41">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="dGWG_sC8McWYThyw6kNz-2" value="Domain Registration" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="620" y="380" width="120" height="80" as="geometry" />
        </mxCell>
        <mxCell id="dGWG_sC8McWYThyw6kNz-25" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="dGWG_sC8McWYThyw6kNz-3" target="dGWG_sC8McWYThyw6kNz-2">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="680" y="280" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="dGWG_sC8McWYThyw6kNz-38" value="Register domain through cloudflare" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=15;" vertex="1" connectable="0" parent="dGWG_sC8McWYThyw6kNz-25">
          <mxGeometry x="-0.2923" y="-2" relative="1" as="geometry">
            <mxPoint x="91" y="38" as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="dGWG_sC8McWYThyw6kNz-26" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="dGWG_sC8McWYThyw6kNz-3" target="dGWG_sC8McWYThyw6kNz-1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="dGWG_sC8McWYThyw6kNz-37" value="Automatically runs workflow" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=15;" vertex="1" connectable="0" parent="dGWG_sC8McWYThyw6kNz-26">
          <mxGeometry x="-0.1475" y="-1" relative="1" as="geometry">
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="dGWG_sC8McWYThyw6kNz-3" value="Github" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="365" y="250" width="120" height="60" as="geometry" />
        </mxCell>
        <mxCell id="dGWG_sC8McWYThyw6kNz-10" value="Domains" style="swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="130" y="460" width="100" height="120" as="geometry" />
        </mxCell>
        <mxCell id="dGWG_sC8McWYThyw6kNz-11" value="Domain1" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;rotatable=0;whiteSpace=wrap;html=1;" vertex="1" parent="dGWG_sC8McWYThyw6kNz-10">
          <mxGeometry y="30" width="100" height="30" as="geometry" />
        </mxCell>
        <mxCell id="dGWG_sC8McWYThyw6kNz-12" value="Domain2" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;rotatable=0;whiteSpace=wrap;html=1;" vertex="1" parent="dGWG_sC8McWYThyw6kNz-10">
          <mxGeometry y="60" width="100" height="30" as="geometry" />
        </mxCell>
        <mxCell id="dGWG_sC8McWYThyw6kNz-13" value="Domain3" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;rotatable=0;whiteSpace=wrap;html=1;" vertex="1" parent="dGWG_sC8McWYThyw6kNz-10">
          <mxGeometry y="90" width="100" height="30" as="geometry" />
        </mxCell>
        <mxCell id="dGWG_sC8McWYThyw6kNz-16" value="Websites" style="swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="20" y="460" width="100" height="120" as="geometry" />
        </mxCell>
        <mxCell id="dGWG_sC8McWYThyw6kNz-17" value="Website1" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;rotatable=0;whiteSpace=wrap;html=1;" vertex="1" parent="dGWG_sC8McWYThyw6kNz-16">
          <mxGeometry y="30" width="100" height="30" as="geometry" />
        </mxCell>
        <mxCell id="dGWG_sC8McWYThyw6kNz-18" value="Website2" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;rotatable=0;whiteSpace=wrap;html=1;" vertex="1" parent="dGWG_sC8McWYThyw6kNz-16">
          <mxGeometry y="60" width="100" height="30" as="geometry" />
        </mxCell>
        <mxCell id="dGWG_sC8McWYThyw6kNz-19" value="Website3" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;rotatable=0;whiteSpace=wrap;html=1;" vertex="1" parent="dGWG_sC8McWYThyw6kNz-16">
          <mxGeometry y="90" width="100" height="30" as="geometry" />
        </mxCell>
        <mxCell id="dGWG_sC8McWYThyw6kNz-23" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="dGWG_sC8McWYThyw6kNz-12" target="dGWG_sC8McWYThyw6kNz-3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="dGWG_sC8McWYThyw6kNz-24" value="Push domains to github" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="dGWG_sC8McWYThyw6kNz-23">
          <mxGeometry x="0.2743" relative="1" as="geometry">
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="dGWG_sC8McWYThyw6kNz-28" value="Actor" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;" vertex="1" parent="1">
          <mxGeometry x="530" y="27.5" width="30" height="70" as="geometry" />
        </mxCell>
        <mxCell id="dGWG_sC8McWYThyw6kNz-35" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0;exitY=0.5;exitDx=0;exitDy=0;exitPerimeter=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="dGWG_sC8McWYThyw6kNz-33" target="dGWG_sC8McWYThyw6kNz-3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="dGWG_sC8McWYThyw6kNz-36" value="Adds domain to github" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=15;" vertex="1" connectable="0" parent="dGWG_sC8McWYThyw6kNz-35">
          <mxGeometry x="-0.2142" relative="1" as="geometry">
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="dGWG_sC8McWYThyw6kNz-33" value="" style="sketch=0;aspect=fixed;pointerEvents=1;shadow=0;dashed=0;html=1;strokeColor=none;labelPosition=center;verticalLabelPosition=bottom;verticalAlign=top;align=center;fillColor=#00188D;shape=mxgraph.azure.computer" vertex="1" parent="1">
          <mxGeometry x="460" y="40" width="50" height="45" as="geometry" />
        </mxCell>
        <mxCell id="dGWG_sC8McWYThyw6kNz-41" value="Cloudflare" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="620" y="520" width="120" height="60" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
