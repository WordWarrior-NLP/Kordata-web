<script>
  import { Link } from "svelte-routing";

    let nav_item_list = ['Services', 'Team']

</script>
<!-- Navigation-->
<nav class="navbar navbar-expand-lg navbar-dark fixed-top" id="mainNav">
    <div class="container">
        <Link class="navbar-brand" to="/">
            <img src="./src/assets/img/homeNewsenseLogo.png" alt="..." id="logo"/>
        </Link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
            Menu
            <i class="fas fa-bars ms-1"></i>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
            <ul class="navbar-nav text-uppercase ms-auto py-4 py-lg-0">
                {#each nav_item_list as nav_item}
                    <li class="nav-item"><a class="nav-link" href={`/#${nav_item.toLowerCase()}`}>{nav_item}</a></li>
                {/each}
            </ul>
        </div>
    </div>
</nav>
<style>
    #logo{
        width : 10rem;
        height: 2rem;
        object-fit: cover;
    }
</style>