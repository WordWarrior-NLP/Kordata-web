
<script>

  import { onMount  } from 'svelte';
  import fastapi from "../lib/api";
  import cytoscape from 'cytoscape';
  import {newestMainTitle, duration} from '../store'; 
	import graphStyle from '../js/graphStyle';

  export let cid;

  function getEvent(){
    return new Promise((resolve, reject)=>{
      fastapi('get', '/api/events/' +cid, {}, (json)=>{
        resolve(json);
      });
    });
  }

  let startdate = ''
  let event_object = {}
  async function get_event(){
    try{
      let json = await getEvent();
      startdate = json.datetime
      $duration = json.days
      return json
    } catch (error){
      console.error("Error fetching the event:", error);
    }
  }

  event_object = get_event() 
  
  function getMainTitleFromEvent() {
    return new Promise((resolve, reject) => {
      fastapi('get', '/api/events/' +cid+'/main_title', {}, (json) => {
        resolve(json);
      });
    });
  }

  let mainTitle = []
  async function get_main_titles() {
    try {
      let json = await getMainTitleFromEvent();
      $newestMainTitle = json[0].title
      // console.log("제목" + $newestMainTitle)
    } catch (error) {
      console.error("Error fetching main titles:", error);
    }
  }

  get_main_titles()

  let data = [];
  function getGraphData() {
    return new Promise((resolve, reject) => {
      fastapi('get', '/api/graph/' + cid + "/data", {}, (json) => {
        resolve(json);
      });
    });
  }
  async function getGraphDataAndUpdate() {
    try {
      const json = await getGraphData();
      data = json;
    } catch (error) {
      console.error("Error fetching graph data:", error);
    }
  }

  let graphCy = null

  onMount(async () => {
    await getGraphDataAndUpdate(); 
    graphCy = cytoscape({
      container: document.getElementById("cy-container"),
      elements: data,
      style : graphStyle,
      layout: {
        nodeSep: 100,
        animate: false,
        avoidOverlap: true,
        name: 'cose',
        idealEdgeLength: 100, // This controls the ideal length of edges
        nodeRepulsion: function(node) {
          return 10000000; // Increase this value to increase the distance between nodes
        }
      },
      zoomingEnabled: true,
      userZoomingEnabled: true,
      autoungrabify: false,
      pan : {x: 400, y: 500},
      wheelSensitivity : 0.3,
    });

    graphCy.on("mouseover", "edge", function (e) {
      e.target.addClass("hover");
    });
    graphCy.on("mouseout", "edge", function (e) {
      e.target.removeClass("hover");
    });
    //NODE EVENTS
    graphCy.on("mouseover", "node", function (e) {
      e.target.addClass("hover");
    });
    graphCy.on("mouseout", "node", function (e) {
      e.target.removeClass("hover");
    });
    graphCy.on("mousedown", "node", function (e) {
      e.target.addClass("hover");
    });
    graphCy.on("click", "node", function (e) {
      graphCy.zoom({level:0.8, position: this.position()})
      graphCy.pan(this.position)
    });
    graphCy.on("click", "edge", function (e) {
      graphCy.zoom({level:0.8, position: this.position()})
    });
});

let value = 0

async function setVisible(){
  try {
      mainTitle = await getMainTitleFromEvent();
      $newestMainTitle = mainTitle[value].title
      // console.log($newestMainTitle)
    } catch (error) {
      console.error("Error fetching main titles:", error);
    }
    graphCy.nodes('node[days]').each(function(node){
      if(node.data("days") < value){
        if(!(node.hasClass("hide"))){
          node.addClass("hide");
          // console.log("hide" + node.data("days"))
        }
      }
      else{
        let opacityValue = Math.max(0.2, Math.min(1, 1- (value- node.data('days')) / $duration));
        if(node.hasClass("hide")){
          node.removeClass("hide")
          node.data('opacity', opacityValue);
        }
      }
    });
  };


  function addDays(startdate, value) {
    const date = new Date(startdate);
    const days = $duration - value;
    date.setDate(date.getDate() + days);

    const year = date.getFullYear();
    const month = String(date.getMonth()+1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');

    const endDateString = `${year}-${month}-${day}`
    return endDateString
}


</script>

<div class="container-fluid" >
  <div id="slider-box" class="w-75">
    <p align="center" class="mb-0">{startdate} ~ {addDays(startdate, value)}</p>
    <input type="range" class="form-range" bind:value min=0 max={$duration} on:change={setVisible}/>
    <p id="maintitle" align="center">Main Title : {$newestMainTitle}</p>
  </div>
  <div id="cy-container"></div>
</div>


<style lang="scss">
  $offset: 187;
  $duration: 1.4s;

.spinner-box{
  margin-top: 16rem;
  display: flex;
  align-items: center;
  justify-content: center;

}

.spinner {
  animation: rotator $duration linear infinite;
}

@keyframes rotator {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(270deg); }
}

.path {
  stroke-dasharray: $offset;
  stroke-dashoffset: 0;
  transform-origin: center;
  animation:
    dash $duration ease-in-out infinite, 
    colors ($duration*4) ease-in-out infinite;
}

@keyframes colors {
  0% { stroke: #4285F4; }
  25% { stroke: #DE3E35; }
  50% { stroke: #F7C223; }
  75% { stroke: #1B9A59; }
  100% { stroke: #4285F4; }
}

@keyframes dash {
 0% { stroke-dashoffset: $offset; }
 50% {
   stroke-dashoffset: calc($offset / 4);
   transform:rotate(135deg);
 }
 100% {
   stroke-dashoffset: $offset;
   transform:rotate(450deg);
 }
}

.container-fluid{
display: flex;
flex-direction: column;
}
#cy-container {
  height: 750px;
  width : 100%;
  min-width: 768px;
  margin: auto;
}
#slider-box {
  margin-top: 5px;
  margin-bottom: 10px;
  margin-left: auto;
  margin-right: auto;
}
</style>