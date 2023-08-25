<script>
  import { Link } from "svelte-routing";
  import Sidebar from "../components/Sidebar.svelte";
  import GraphContainer from "../components/GraphContainer.svelte";
  import { sideActive } from "../store";
  $sideActive = true;
  console.log($sideActive)

  export let cid;

</script>
<section class="bg-light" id="event">
  <div class="d-flex h-100" id="wrapper" class:toggled={$sideActive}>
    <!-- Sidebar -->
     <Sidebar cid={cid}></Sidebar>
    <!-- Page content wrapper-->
    <div id="page-content-wrapper">
        <!-- Top navigation-->
        <nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
            <div class="container-fluid">
                <button class="btn btn-primary" id="menu-toggle" on:click={() => $sideActive=!($sideActive)}>기사 보기</button>
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
        <GraphContainer cid = {cid}></GraphContainer>
    </div>
  </div>
</section>

<style>
    #event {
        padding: 0;
    }
    #menu-toggle{
      font-weight:700;
    }
</style>