<script>
  import { Link } from "svelte-routing";
  import Sidebar from "../components/Sidebar.svelte";

  let sideActive = false;

  export let cid;
  // let cid = parseInt(params.cid)
  console.log(cid)
  import fastapi from "../lib/api";    

  let news_list = []
  function getNewsFromEvent() {
    return new Promise((resolve, reject) => {
      fastapi('get', '/api/events/' +cid+'/news', {}, (json) => {
        resolve(json);
        reject(json)
      });
    });
  }

  async function get_news_list() {
      try {
        let json = await getNewsFromEvent();
        news_list = [...news_list, ...json];
      } catch (error) {
        console.error("Error fetching news:", error);
      }
    }

  get_news_list()

</script>
<section class="bg-light" id="event">
  <div class="d-flex h-100" id="wrapper" class:toggled={sideActive}>
    <!-- Sidebar -->
     <Sidebar news_list={news_list}></Sidebar>
    <!-- Page content wrapper-->
    <div id="page-content-wrapper">
        <!-- Top navigation-->
        <nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
            <div class="container-fluid">
                <button class="btn btn-primary" id="menu-toggle" on:click={() => sideActive=!sideActive}>Toggle Menu</button>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav ms-auto mt-2 mt-lg-0">
                        <li class="nav-item active"><Link class="nav-link" to="/">Home</Link></li>
                        <li class="nav-item"><Link class="nav-link" to="/events">Events</Link></li>
                    </ul>
                </div>
            </div>
        </nav>
        <!-- Page content-->
        <div class="container-fluid">
            <h1 class="mt-4">Simple Sidebar</h1>
            <p>The starting state of the menu will appear collapsed on smaller screens, and will appear non-collapsed on larger screens. When toggled using the button below, the menu will change.</p>
            <p>
                Make sure to keep all page content within the
                <code>#page-content-wrapper</code>
                . The top navbar is optional, and just for demonstration. Just create an element with the
                <code>#sidebarToggle</code>
                ID which will toggle the menu when clicked.
            </p>
        </div>
    </div>
  </div>
</section>

<style>
    #event {
        padding: 0;
    }
</style>