<script>
    import CardImage from "../components/CardImage.svelte";
    import CardText from "../components/CardText.svelte";
    import Clients from "../components/Clients.svelte";
    import Footer from "../components/Footer.svelte";
    import Masthead from "../components/Masthead.svelte";
    import Navbar from "../components/Navbar.svelte";
    import Profile from "../components/Profile.svelte";
    import Timeline from "../components/Timeline.svelte";
    import fastapi from "../lib/api"

    let event_list = []

    function get_event_list() {
        fastapi('get', '/api/events/list', {}, (json) => {
            event_list = json
        })
    }

    get_event_list()
</script>

<Navbar/>
<Masthead/>
<CardText/>
<CardImage/>
<!-- TODO event_list를 CardImage의 변수로 만들기 -->
<ul>
    {#each event_list as event}
        <li>{event.name}</li>
    {/each}
</ul>
<Timeline/>
<Profile/>
<Clients/>
<Footer/>