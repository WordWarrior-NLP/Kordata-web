<script>
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"
  import Navbar from "./components/Navbar.svelte";
  import Footer from "./components/Footer.svelte";
  import NotFound from './routes/NotFound.svelte';
  import Event from './routes/Event.svelte';
  const routes = {
    '/': Home,
    "/events/:id" : Event,
    '*' : NotFound,
  }
</script>
<Navbar/>
<Router {routes}/>
<Footer/>