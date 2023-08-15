<script>
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"
  import Navbar from "./components/Navbar.svelte";
  import Footer from "./components/Footer.svelte";
  const routes = {
    '/': Home,
    // '/Event': Diagram,
  }
</script>
<Navbar/>
<Router {routes}/>
<Footer/>