<div class="container-fluid">
    <div id="sigma-container"></div>
</div><!-- 사건 노드 정보 -->
<script>
    import Sigma from 'sigma';
    import Graph from 'graphology';
    import { onMount } from 'svelte';

    onMount(()=>{
        const container1 =  document.getElementById("sigma-container");
        const graph = new Graph();

        graph.addNode("Event", {x: 0, y: 10, size: 30, label: "Event", color: "blue"})
        graph.addNode("Entity1", { x: 10, y: 0, size: 10, label: "Entity1", color: "green" });
        graph.addNode("Entity2", { x: 7, y: 9, size: 10, label: "Entity2", color: "red" });
        graph.addNode("Entity3", { x: -7, y: -6, size: 10, label: "Entity3", color: "teal" });

// here there are different relations between nodes. 
        graph.addEdge("Event", "Entity1");
        graph.addEdge("Event", "Entity2");
        graph.addEdge("Event", "Entity3");

        const renderer = new Sigma(graph, container1);

    })
    
</script>

<style>
#sigma-container {
  height: 900px;
}
#sigma-container canvas{
  width: 100%;
  height: 900px;
}
</style>