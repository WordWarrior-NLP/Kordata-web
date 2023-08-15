<script>
    import CardImage from "../components/CardImage.svelte";
    import CardText from "../components/CardText.svelte";
    import Masthead from "../components/Masthead.svelte";
    import fastapi from "../lib/api"

    let event_list = []

    function get_event_list() {
        fastapi('get', '/api/events/list', {}, (json) => {
            event_list = json
        })
    }

    get_event_list()
</script>
<Masthead/>
<CardText/>
<CardImage {event_list}/>
