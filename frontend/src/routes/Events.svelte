<script>
    import fastapi from "../lib/api"
    import Navbar from "../components/Navbar.svelte";   
    import CardImage from "../components/CardImage.svelte";
    let eventList = []
    function get_event_list() {
        fastapi('get', '/api/events/list', {}, (json) => {
            eventList = json
        })
    }
    get_event_list()
</script>

<!-- Events Grid-->
<Navbar/>
<section class="page-section bg-light" id="portfolio">
    <div class="container">
        <div class="text-center">
            <h2 class="section-heading text-uppercase">TOP 25 사건</h2>
            <h3 class="section-subheading text-muted">최근 일어난 주요 정치 사건들을 살펴봅시다</h3>
        </div>
        <CardImage eventList={eventList}/>
    </div>
</section>