<script>
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"
  import Footer from "./components/Footer.svelte";
  import NotFound from './routes/NotFound.svelte';
  import Event from './routes/Event.svelte';
  import {previousLocation} from './store'
  const routes = {
    '/': Home,
    "/events/:id" : Event,
    '*' : NotFound,
  }

  function routeLoaded(event){
    let currentLocation = event.detail.location;
    if ($previousLocation != currentLocation){
        window.scrollTo(0,0)
    }
    $previousLocation = currentLocation;
  }

</script>
<Router {routes} on:routeLoaded={routeLoaded}/>
<Footer/>