<script>
  import { Router, Route } from "svelte-routing"; 
  import Home from "./routes/Home.svelte";
  import Footer from "./components/Footer.svelte";
  import NotFound from './routes/NotFound.svelte';
  import Diagram from './routes/Diagram.svelte';
  import Events from './routes/Events.svelte';
  import {previousLocation} from './store'
  export let url = "";

  function routeLoaded(event){
    let currentLocation = event.detail.location;
    if ($previousLocation != currentLocation){
        window.scrollTo(0,0)
    }
    $previousLocation = currentLocation;
  }

</script>
<Router url={url}>
  <Route path = "/"><Home/></Route>
  <Route path = "/events" component="{Events}"on:routeLoaded={routeLoaded} ></Route>
  <Route path = "/events/:cid" component="{Diagram}" on:routeLoaded={routeLoaded}></Route>
  <Route path = "*" component="{NotFound}"></Route>
</Router>
<Footer/>