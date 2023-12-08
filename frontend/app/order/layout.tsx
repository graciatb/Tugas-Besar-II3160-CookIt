'use client'

import SideNav from '../component/sidebar2'
import { Box, Flex } from "@chakra-ui/react";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
    return (
          <body>
          <Flex>
          <SideNav />
          <Box flex="5" pl="10">
            {children}
          </Box>
        </Flex>
          </body>
      )
}
