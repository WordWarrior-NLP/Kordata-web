export default [
    //CORE
{
  selector: "core",
  css: {
    "active-bg-size": 0 //The size of the active background indicator.
  }
},
// node
{
  selector: 'node',
  css: {
    'label': 'data(label)',
    'color': "white",
    'text-halign' : 'center',
    'text-valign' : 'center',
    "text-max-width": "100px",
    "padding-top": "10px",
    "padding-left": "10px",
    "padding-bottom": "10px",
    "padding-right": "10px"

  }
},
{
  selector: 'node[opacity]',
  css:{
    'background-opacity' : 'data(opacity)',
  },
},
{
  selector:'node[level=3]',
  style:{
    'z-index' : 999,
    'shape' : 'round-rectangle',
    'width' : 'label',
    'height' : '150px',
    'font-weight' : '900',
    'font-size' : '40px',
    'text-outline-width' : "3px",
    "text-outline-color" : '#015839',
    'color': "white",
    'background-color' : '#015839',

  }
},
{  
  selector:'node[level=2]',
  style:{
    'width' : '100px',
    'height' : '100px',
    'z-index' : 20,
    'font-weight' : '600',
    'font-size' : '25px',
    'background-color' : '#FF9326',
    'text-outline-width' : "2px",
    "text-outline-color" : "#Ff9326",
  }
},
{  
  selector:'node[level=1]',
  style:{
    'background-color' : '#c0c0c0',
    'color' : "black"
  }
},
{
  selector:'node[opacity]',
  style:{
    'background-opacity' : 'data(opacity)'
  }
},
{
  selector: 'node.hover',
  css:{
    "background-opacity": 1,
    "z-index" : 100,
    "padding" : '30px',
  }
},
{
  selector: 'edge',
  style: {
    'width': 2,
    'target-endpoint' : 'outside-to-node-or-label',
    'source-endpoint' : 'outside-to-node-or-label',
    'source-arrow-shape': 'vee',
    'line-opacity' : 0.3,
  }
},
{
  selector : 'edge[polarity > 0]',
  style:{
    'line-color' : '#1290ff'
  }
},
{
  selector : 'edge[polarity < 0]',
  style:{
    'line-color' : '#ff4646'
  }
},
{ selector: 'edge[polarity = 0]',
  style: {
    'line-color' : '#ebff86'
  }
},
{
  selector: 'edge.hover',
  style:{
    'width' : 10,
    'line-opacity' : 0.5,
    'z-index' : 10
  }
},
{
  selector: 'edge:selected',
  style:{
    'width' : 15,
    'line-opacity' : 0.7,
    'z-index' : 30,
  }
},
{
    selector:'node.hide',
    style:{
        display : 'none'
    }
},


]