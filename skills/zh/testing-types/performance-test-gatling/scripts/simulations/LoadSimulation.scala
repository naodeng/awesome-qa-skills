package simulations

import io.gatling.core.Predef._
import scala.concurrent.duration._

class LoadSimulation extends BaseSimulation {

  private val loadScenario = scenario(s"load-homepage-$envName")
    .forever {
      homepageChain("load")
    }

  setUp(
    loadScenario.injectOpen(
      rampUsersPerSec(1).to(30).during(2.minutes),
      constantUsersPerSec(40).during(5.minutes),
      rampUsersPerSec(40).to(1).during(2.minutes)
    )
  ).protocols(httpProtocol)
    .assertions(
      global.failedRequests.percent.lt(1.0),
      global.responseTime.percentile3.lt(800),
      global.responseTime.percentile4.lt(1500)
    )
}
