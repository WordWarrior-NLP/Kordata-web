<script>
    import { Link } from "svelte-routing";
    export let event_list
</script>

<!-- Events Grid-->
<div class="row">
    {#each event_list as item}
        <div class="col-lg-4 col-sm-6 mb-4">
            <div class="portfolio-item">
                <Link to="/events/{item.cid}" class="portfolio-link">
                    <div class="portfolio-hover">
                        <div class="portfolio-hover-content"><i class="fas fa-plus fa-3x"></i></div>
                    </div>
                    <div class="portfolio-caption">
                        {#each item.name as name}
                            <div class="portfolio-caption-heading">#{name}</div>
                        {/each}
                        <div class="portfolio-caption-subheading text-muted">{item.datetime} ~ </div>
                    </div>
                </Link>
            </div>
        </div>
    {/each}
</div>
