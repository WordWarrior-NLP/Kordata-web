<script>
  import { Link } from "svelte-routing";
  import Sidebar from "../components/Sidebar.svelte";
  import fastapi from "../lib/api";   
  import GraphContainer from "../components/GraphContainer.svelte";
  import { onMount } from 'svelte';
  let sideActive = false;

  export let cid;
  import { tick } from 'svelte';

  function getMainTitleFromEvent() {
    return new Promise((resolve, reject) => {
      fastapi('get', '/api/events/' +cid+'/with_title', {}, (json) => {
        resolve(json);
      });
    });
  }
  
  let event_with_title = {
    main_titles: []
  }
  async function get_main_titles() {
    try {
      let json = await getMainTitleFromEvent();
      event_with_title = json
      console.log(event_with_title.main_titles)
    } catch (error) {
      console.error("Error fetching main titles:", error);
    }
  }
  get_main_titles()
  
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
        <GraphContainer event_with_title={event_with_title}></GraphContainer>
    </div>
  </div>
</section>

<style>
    #event {
        padding: 0;
    }
</style>