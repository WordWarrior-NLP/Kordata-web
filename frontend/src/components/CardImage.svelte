<script>
    export let event_list
    import {link} from 'svelte-spa-router'
</script>

<!-- Events Grid-->
<section class="page-section bg-light" id="portfolio">
    <div class="container">
        <div class="text-center">
            <h2 class="section-heading text-uppercase">TOP 10 사건</h2>
            <h3 class="section-subheading text-muted">Lorem ipsum dolor sit amet consectetur.</h3>
        </div>
        <div class="row">
            {#each event_list as item}
                <div class="col-lg-4 col-sm-6 mb-4">
                    <div class="portfolio-item">
                        <a use:link href="/events/:{item.cid}" class="portfolio-link" >
                            <div class="portfolio-hover">
                                <div class="portfolio-hover-content"><i class="fas fa-plus fa-3x"></i></div>
                            </div>
                            <div class="portfolio-caption">
                                {#each item.name as name}
                                    <div class="portfolio-caption-heading">#{name}</div>
                                {/each}
                                <div class="portfolio-caption-subheading text-muted">{item.datetime} ~ </div>
                            </div>
                        </a>
                    </div>
                </div>
            {/each}
        </div>
    </div>
</section>