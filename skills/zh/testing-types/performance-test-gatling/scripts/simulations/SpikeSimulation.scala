package simulations

import io.gatling.core.Predef._
import scala.concurrent.duration._

class SpikeSimulation extends BaseSimulation {

  private val spikeScenario = scenario(s"spike-homepage-$envName")
    .forever {
      homepageChain("spike")
    }

  setUp(
    spikeScenario.injectOpen(
      rampUsersPerSec(1).to(20).during(1.minute),
      rampUsersPerSec(20).to(250).during(30.seconds),
      constantUsersPerSec(250).during(2.minutes),
      rampUsersPerSec(250).to(20).during(30.seconds),
      constantUsersPerSec(20).during(2.minutes)
    )
  ).protocols(httpProtocol)
    .assertions(
      global.failedRequests.percent.lt(5.0),
      global.responseTime.percentile3.lt(1500),
      global.responseTime.percentile4.lt(3000)
    )
}
