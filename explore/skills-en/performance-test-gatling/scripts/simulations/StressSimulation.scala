package simulations

import io.gatling.core.Predef._
import scala.concurrent.duration._

class StressSimulation extends BaseSimulation {

  private val stressScenario = scenario(s"stress-homepage-$envName")
    .forever {
      homepageChain("stress")
    }

  setUp(
    stressScenario.injectOpen(
      rampUsersPerSec(1).to(80).during(2.minutes),
      rampUsersPerSec(80).to(180).during(3.minutes),
      rampUsersPerSec(180).to(260).during(3.minutes),
      rampUsersPerSec(260).to(1).during(2.minutes)
    )
  ).protocols(httpProtocol)
    .assertions(
      global.failedRequests.percent.lt(3.0),
      global.responseTime.percentile3.lt(1200),
      global.responseTime.percentile4.lt(2500)
    )
}
