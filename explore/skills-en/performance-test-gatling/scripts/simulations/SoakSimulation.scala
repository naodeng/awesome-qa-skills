package simulations

import io.gatling.core.Predef._
import scala.concurrent.duration._

class SoakSimulation extends BaseSimulation {

  private val soakScenario = scenario(s"soak-homepage-$envName")
    .forever {
      homepageChain("soak")
    }

  setUp(
    soakScenario.injectOpen(
      constantUsersPerSec(60).during(30.minutes)
    )
  ).protocols(httpProtocol)
    .assertions(
      global.failedRequests.percent.lt(2.0),
      global.responseTime.percentile3.lt(900),
      global.responseTime.percentile4.lt(1800)
    )
}
