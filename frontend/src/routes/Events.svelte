<script>
    import fastapi from "../lib/api"
    import Navbar from "../components/Navbar.svelte";   
    import CardImage from "../components/CardImage.svelte";
    let event_list = []
    function get_event_list() {
        fastapi('get', '/api/events/list', {}, (json) => {
            event_list = json
        })
    }
    get_event_list()
</script>

<!-- Events Grid-->
<Navbar/>
<section class="page-section bg-light" id="portfolio">
    <div class="container">
        <div class="text-center">
            <h2 class="section-heading text-uppercase">TOP 10 사건</h2>
            <h3 class="section-subheading text-muted">Lorem ipsum dolor sit amet consectetur.</h3>
        </div>
        <CardImage event_list={event_list}/>
    </div>
</section>