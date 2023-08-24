
<script>

  import { onMount  } from 'svelte';
  import fastapi from "../lib/api";
  import cytoscape from 'cytoscape';
  import {newestMainTitle, duration} from '../store'; 
	import graphStyle from '../js/graphStyle';

  export let cid;
  let isLoadingGraphData =true;

  function getEvent(){
    return new Promise((resolve, reject)=>{
      fastapi('get', '/api/events/' +cid, {}, (json)=>{
        resolve(json);
      });
    });
  }

  let startdate = ''
async function get_event(){
    try{
      let json = await getEvent();
      startdate = json.datetime
      $duration = json.days
    } catch (error){
      console.error("Error fetching the event:", error);
    }
  }
  
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
      for (let obj of json){
        mainTitle.push(obj.title)
      }
    } catch (error) {
      console.error("Error fetching main titles:", error);
    }
  }

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

  let graphCy = null;

  onMount(async () => {
    try {
      await Promise.all([
        get_event(),
        get_main_titles()
      ]);
    
      isLoadingGraphData = false;
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
          idealEdgeLength: 300, // This controls the ideal length of edges
          nodeRepulsion: function(node) {
            return 100000000; // Increase this value to increase the distance between nodes
          }
        },
        zoomingEnabled: true,
        userZoomingEnabled: true,
        autoungrabify: false,
        zoom:1,
        pan : {x: 400, y: 100},
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
    
    } catch (error) {
      console.error("Error setting visibility:", error);
    }
  });

let value = 0

async function setVisible(){
  try {
      $newestMainTitle = mainTitle[value]
    } catch (error) {
      console.error("Error fetching main titles:", error);
    }
    graphCy.nodes('node[days]').each(function(node){
      if(node.data("days") < value){
        if(!(node.hasClass("hide"))){
          node.addClass("hide");
        }
      }
      else{
        let opacityValue = Math.max(0.3, Math.min(1, 1- (value- node.data('days')) / $duration));
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
    <p align="center" id="sliderValue">{startdate} ~ {addDays(startdate, value)}</p>
    <input type="range" class="form-range" bind:value min=0 max={$duration} on:change={setVisible}/>
    <p id="mainTitle" align="center">Main Title : {$newestMainTitle}</p>
  </div>
  {#if isLoadingGraphData}
      <div class="spinner-box">
        <svg class="spinner" width="65px" height="65px" viewBox="0 0 66 66" xmlns="http://www.w3.org/2000/svg">
          <circle class="path" fill="none" stroke-width="6" stroke-linecap="round" cx="33" cy="33" r="30"></circle>
       </svg>
      </div>
  {:else}
    <div id="cy-container"></div>
  {/if}
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
  0% { stroke: #fa6b05; }
  25% { stroke: #ff8f26f1; }
  50% { stroke: #f7ad23; }
  75% { stroke: #f8c572; }
  100% { stroke: #f6e1af; }
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
#sliderValue{
  margin-top: 1rem;
  margin-bottom: 0;
  text-align: center;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-weight: 600;
}
#mainTitle{
  font-size: large;
  font-weight: 600;
}
</style>